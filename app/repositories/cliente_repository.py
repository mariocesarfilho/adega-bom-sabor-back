from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from app.models.cliente import Cliente
from app.models.compra import Compra


class ClienteRepository:
    """Repository for customer data access.
    
    Estrutura baseada na planilha Cliente.xlsx.
    """
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> List[Cliente]:
        """Get all customers."""
        return self.db.query(Cliente).all()
    
    def get_by_id(self, cliente_id: int) -> Optional[Cliente]:
        """Get customer by ID."""
        return self.db.query(Cliente).filter(Cliente.cliente_id == cliente_id).first()
    
    def get_count(self) -> int:
        """Get total number of customers."""
        return self.db.query(func.count(Cliente.cliente_id)).scalar()
    
    def get_by_cidade(self) -> List[dict]:
        """Get customer count by city."""
        result = self.db.query(
            Cliente.cidade,
            func.count(Cliente.cliente_id).label('quantidade')
        ).group_by(Cliente.cidade).all()
        
        return [{"cidade": r.cidade, "quantidade": r.quantidade} for r in result]
    
    def get_customer_features(self, cliente_id: int) -> dict:
        """Get customer features for ML models.
        
        Features incluem:
        - frequencia_compra (total_compras)
        - dias_desde_ultima_compra (recencia)
        - ticket_medio = SUM(valor) / COUNT(compras)
        - cancelou_assinatura (label para churn)
        """
        cliente = self.get_by_id(cliente_id)
        if not cliente:
            return None
        
        # Get purchase statistics
        stats = self.db.query(
            func.count(Compra.compra_id).label('total_compras'),
            func.coalesce(func.sum(Compra.valor), 0).label('valor_total'),
            func.coalesce(func.sum(Compra.quantidade), 0).label('qtd_total'),
            func.max(Compra.data_compra).label('ultima_compra')
        ).filter(Compra.cliente_id == cliente_id).first()
        
        total_compras = stats.total_compras or 0
        valor_total = float(stats.valor_total or 0)
        ticket_medio = valor_total / total_compras if total_compras > 0 else 0
        
        return {
            'cliente_id': cliente.cliente_id,
            'idade': cliente.idade,
            'pontuacao_engajamento': cliente.pontuacao_engajamento,
            'assinante': 1 if cliente.assinante_clube else 0,
            'cancelou_assinatura': 1 if cliente.cancelou_assinatura else 0,
            'total_compras': total_compras,
            'valor_total': valor_total,
            'ticket_medio': ticket_medio,
            'qtd_total': stats.qtd_total or 0,
            'ultima_compra': stats.ultima_compra
        }
    
    def get_all_customer_features(self) -> List[dict]:
        """Get features for all customers for ML training."""
        clientes = self.get_all()
        features = []
        
        for cliente in clientes:
            feature = self.get_customer_features(cliente.cliente_id)
            if feature:
                features.append(feature)
        
        return features
    
    def get_inativos(self, dias_limite: int = 60) -> List[Cliente]:
        """Get customers inactive for more than dias_limite days.
        
        Regra simbolica: SE cliente > 60 dias sem comprar -> marcar como inativo.
        """
        from datetime import datetime, timedelta
        data_limite = datetime.now().date() - timedelta(days=dias_limite)
        
        # Subquery to get last purchase date per customer
        subquery = self.db.query(
            Compra.cliente_id,
            func.max(Compra.data_compra).label('ultima_compra')
        ).group_by(Compra.cliente_id).subquery()
        
        # Get customers whose last purchase is older than data_limite
        result = self.db.query(Cliente).join(
            subquery, Cliente.cliente_id == subquery.c.cliente_id
        ).filter(subquery.c.ultima_compra < data_limite).all()
        
        return result
