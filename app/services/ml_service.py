import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime
from typing import Optional, List
from sqlalchemy.orm import Session
from app.repositories import ClienteRepository


class MLService:
    """Service for Machine Learning models (churn prediction and segmentation)."""
    
    def __init__(self):
        self.churn_model: Optional[RandomForestClassifier] = None
        self.segmentation_model: Optional[KMeans] = None
        self.scaler: Optional[StandardScaler] = None
        self.is_trained: bool = False
    
    def train_models(self, db: Session) -> bool:
        """Train ML models using data from database."""
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
                
                valor_medio = f['valor_total'] / f['total_compras'] if f['total_compras'] > 0 else 0
                
                customer_features.append({
                    'cliente_id': f['cliente_id'],
                    'idade': f['idade'],
                    'pontuacao_engajamento': f['pontuacao_engajamento'],
                    'assinante': f['assinante'],
                    'total_compras': f['total_compras'],
                    'valor_total': f['valor_total'],
                    'valor_medio': valor_medio,
                    'qtd_total': f['qtd_total'],
                    'recencia': recencia
                })
            
            df_features = pd.DataFrame(customer_features)
            
            # Features for clustering
            feature_cols = ['idade', 'pontuacao_engajamento', 'total_compras', 'valor_total', 'valor_medio', 'recencia']
            X = df_features[feature_cols].values
            
            # Scale features
            self.scaler = StandardScaler()
            X_scaled = self.scaler.fit_transform(X)
            
            # Train segmentation model (KMeans with 3 clusters)
            self.segmentation_model = KMeans(n_clusters=3, random_state=42, n_init=10)
            self.segmentation_model.fit(X_scaled)
            
            # Train churn prediction model
            # Create synthetic churn labels based on engagement and recency
            y_churn = []
            for _, row in df_features.iterrows():
                churn_prob = (10 - row['pontuacao_engajamento']) / 10 * 0.5 + (row['recencia'] / 365) * 0.5
                y_churn.append(1 if churn_prob > 0.5 else 0)
            
            self.churn_model = RandomForestClassifier(n_estimators=50, random_state=42)
            self.churn_model.fit(X_scaled, y_churn)
            
            self.is_trained = True
            print("ML models trained successfully")
            return True
            
        except Exception as e:
            print(f"Error training models: {e}")
            return False
    
    def get_customer_features_array(self, db: Session, cliente_id: int) -> Optional[np.ndarray]:
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
        
        valor_medio = features['valor_total'] / features['total_compras'] if features['total_compras'] > 0 else 0
        
        feature_array = np.array([[
            features['idade'],
            features['pontuacao_engajamento'],
            features['total_compras'],
            features['valor_total'],
            valor_medio,
            recencia
        ]])
        
        return self.scaler.transform(feature_array)
    
    def predict_churn(self, db: Session, cliente_id: int) -> float:
        """Predict churn probability for a customer."""
        if not self.is_trained:
            return 0.5
        
        features_scaled = self.get_customer_features_array(db, cliente_id)
        if features_scaled is None:
            return 0.5
        
        proba = self.churn_model.predict_proba(features_scaled)[0]
        
        # Handle case where model only has one class
        if len(proba) == 1:
            cliente_repo = ClienteRepository(db)
            features = cliente_repo.get_customer_features(cliente_id)
            if features:
                recencia = (datetime.now().date() - features['ultima_compra']).days if features['ultima_compra'] else 365
                churn_score = (10 - features['pontuacao_engajamento']) / 10 * 0.5 + (recencia / 365) * 0.5
                return float(min(max(churn_score, 0), 1))
            return 0.5
        
        return float(proba[1])
    
    def predict_segment(self, db: Session, cliente_id: int) -> dict:
        """Predict customer segment."""
        if not self.is_trained:
            return {"segmento": "Desconhecido", "descricao": "Modelos nao treinados"}
        
        features_scaled = self.get_customer_features_array(db, cliente_id)
        if features_scaled is None:
            return {"segmento": "Desconhecido", "descricao": "Dados insuficientes"}
        
        cluster = self.segmentation_model.predict(features_scaled)[0]
        
        segment_names = {
            0: {"segmento": "Premium", "descricao": "Clientes de alto valor com compras frequentes e alto engajamento"},
            1: {"segmento": "Sensivel a Promocoes", "descricao": "Clientes que respondem bem a ofertas e descontos"},
            2: {"segmento": "Ocasional", "descricao": "Clientes com compras esporadicas, potencial de crescimento"}
        }
        
        return segment_names.get(cluster, {"segmento": "Desconhecido", "descricao": "Segmento nao identificado"})
