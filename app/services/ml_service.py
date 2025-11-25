import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime
from typing import Optional, List
from sqlalchemy.orm import Session
from app.repositories import ClienteRepository


class MLService:
    """Service for Machine Learning models (churn prediction and segmentation).
    
    Modelos implementados:
    - Predicao de Churn: RandomForest usando cancelou_assinatura como label real
    - Segmentacao: KMeans com 3 clusters (Premium, Sensivel a Promocoes, Ocasional)
    
    Features utilizadas:
    - frequencia_compra (total_compras)
    - ticket_medio = SUM(valor) / COUNT(compras)
    - dias_desde_ultima_compra (recencia)
    - pontuacao_engajamento
    - assinante_clube
    """
    
    def __init__(self):
        self.churn_model: Optional[RandomForestClassifier] = None
        self.segmentation_model: Optional[KMeans] = None
        self.scaler: Optional[StandardScaler] = None
        self.scaler_churn: Optional[StandardScaler] = None
        self.is_trained: bool = False
    
    def train_models(self, db: Session) -> bool:
        """Train ML models using data from database.
        
        Usa cancelou_assinatura como label REAL para o modelo de churn,
        conforme especificado nas instrucoes do projeto.
        """
        try:
            cliente_repo = ClienteRepository(db)
            features_list = cliente_repo.get_all_customer_features()
            
            if len(features_list) == 0:
                print("No customer data available for training")
                return False
            
            # Calculate recency and prepare features
            customer_features = []
            for f in features_list:
                if f['ultima_compra']:
                    recencia = (datetime.now().date() - f['ultima_compra']).days
                else:
                    recencia = 365
                
                customer_features.append({
                    'cliente_id': f['cliente_id'],
                    'idade': f['idade'],
                    'pontuacao_engajamento': f['pontuacao_engajamento'],
                    'assinante': f['assinante'],
                    'cancelou_assinatura': f['cancelou_assinatura'],
                    'total_compras': f['total_compras'],
                    'valor_total': f['valor_total'],
                    'ticket_medio': f['ticket_medio'],
                    'qtd_total': f['qtd_total'],
                    'recencia': recencia
                })
            
            df_features = pd.DataFrame(customer_features)
            
            # Features for segmentation (clustering)
            # Usar: ticket_medio, quantidade de compras, recorrencia
            segment_feature_cols = ['ticket_medio', 'total_compras', 'recencia', 'pontuacao_engajamento']
            X_segment = df_features[segment_feature_cols].values
            
            # Scale features for segmentation
            self.scaler = StandardScaler()
            X_segment_scaled = self.scaler.fit_transform(X_segment)
            
            # Train segmentation model (KMeans with 3 clusters)
            self.segmentation_model = KMeans(n_clusters=3, random_state=42, n_init=10)
            self.segmentation_model.fit(X_segment_scaled)
            
            # Features for churn prediction
            # Usar: frequencia de compras, ticket medio, tempo desde ultima compra, engajamento, assinante
            churn_feature_cols = ['total_compras', 'ticket_medio', 'recencia', 'pontuacao_engajamento', 'assinante']
            X_churn = df_features[churn_feature_cols].values
            
            # Scale features for churn
            self.scaler_churn = StandardScaler()
            X_churn_scaled = self.scaler_churn.fit_transform(X_churn)
            
            # Use REAL cancelou_assinatura as label (not synthetic!)
            y_churn = df_features['cancelou_assinatura'].values
            
            # Train churn prediction model (RandomForest)
            self.churn_model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
            self.churn_model.fit(X_churn_scaled, y_churn)
            
            self.is_trained = True
            print("ML models trained successfully with REAL cancelou_assinatura labels")
            return True
            
        except Exception as e:
            print(f"Error training models: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def get_customer_features_array(self, db: Session, cliente_id: int, for_churn: bool = False) -> Optional[np.ndarray]:
        """Get scaled features array for a customer."""
        if not self.is_trained:
            return None
        
        cliente_repo = ClienteRepository(db)
        features = cliente_repo.get_customer_features(cliente_id)
        
        if not features:
            return None
        
        if features['ultima_compra']:
            recencia = (datetime.now().date() - features['ultima_compra']).days
        else:
            recencia = 365
        
        if for_churn:
            # Features for churn prediction
            feature_array = np.array([[
                features['total_compras'],
                features['ticket_medio'],
                recencia,
                features['pontuacao_engajamento'],
                features['assinante']
            ]])
            return self.scaler_churn.transform(feature_array)
        else:
            # Features for segmentation
            feature_array = np.array([[
                features['ticket_medio'],
                features['total_compras'],
                recencia,
                features['pontuacao_engajamento']
            ]])
            return self.scaler.transform(feature_array)
    
    def predict_churn(self, db: Session, cliente_id: int) -> float:
        """Predict churn probability for a customer.
        
        Retorna probabilidade de churn (0 a 1) baseada no modelo treinado
        com os dados reais de cancelou_assinatura.
        """
        if not self.is_trained:
            return 0.5
        
        features_scaled = self.get_customer_features_array(db, cliente_id, for_churn=True)
        if features_scaled is None:
            return 0.5
        
        proba = self.churn_model.predict_proba(features_scaled)[0]
        
        # Handle case where model only has one class
        if len(proba) == 1:
            # Fallback: use heuristic based on engagement and recency
            cliente_repo = ClienteRepository(db)
            features = cliente_repo.get_customer_features(cliente_id)
            if features:
                recencia = (datetime.now().date() - features['ultima_compra']).days if features['ultima_compra'] else 365
                churn_score = (10 - features['pontuacao_engajamento']) / 10 * 0.5 + (recencia / 365) * 0.5
                return float(min(max(churn_score, 0), 1))
            return 0.5
        
        return float(proba[1])
    
    def predict_segment(self, db: Session, cliente_id: int) -> dict:
        """Predict customer segment using KMeans clustering.
        
        Segmentos:
        - Premium: Clientes de alto valor com compras frequentes
        - Sensivel a Promocoes: Clientes que respondem bem a ofertas
        - Ocasional: Clientes com compras esporadicas
        """
        if not self.is_trained:
            return {"segmento": "Desconhecido", "descricao": "Modelos nao treinados"}
        
        features_scaled = self.get_customer_features_array(db, cliente_id, for_churn=False)
        if features_scaled is None:
            return {"segmento": "Desconhecido", "descricao": "Dados insuficientes"}
        
        cluster = self.segmentation_model.predict(features_scaled)[0]
        
        segment_names = {
            0: {"segmento": "Premium", "descricao": "Clientes de alto valor com compras frequentes e alto engajamento"},
            1: {"segmento": "Sensivel a Promocoes", "descricao": "Clientes que respondem bem a ofertas e descontos"},
            2: {"segmento": "Ocasional", "descricao": "Clientes com compras esporadicas, potencial de crescimento"}
        }
        
        return segment_names.get(cluster, {"segmento": "Desconhecido", "descricao": "Segmento nao identificado"})
