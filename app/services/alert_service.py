from typing import List
from sqlalchemy.orm import Session
from app.repositories import ClienteRepository, ProdutoRepository
from app.services.ml_service import MLService


class AlertService:
    """Service for generating strategic alerts."""
    
    def __init__(self, ml_service: MLService):
        self.ml_service = ml_service
    
    def generate_alerts(self, db: Session) -> List[dict]:
        """Generate all strategic alerts."""
        alerts = []
        
        # Low stock alerts
        alerts.extend(self._generate_stock_alerts(db))
        
        # Churn risk alerts
        alerts.extend(self._generate_churn_alerts(db))
        
        return alerts
    
    def _generate_stock_alerts(self, db: Session) -> List[dict]:
        """Generate alerts for low stock products."""
        produto_repo = ProdutoRepository(db)
        low_stock_products = produto_repo.get_low_stock(threshold=20)
        
        alerts = []
        for produto in low_stock_products:
            severidade = "alta" if produto.estoque < 10 else "media"
            alerts.append({
                "tipo": "estoque_baixo",
                "severidade": severidade,
                "mensagem": f"Produto '{produto.nome}' com estoque baixo: {produto.estoque} unidades",
                "produto_id": produto.produto_id,
                "cliente_id": None
            })
        
        return alerts
    
    def _generate_churn_alerts(self, db: Session) -> List[dict]:
        """Generate alerts for customers with high churn risk."""
        cliente_repo = ClienteRepository(db)
        clientes = cliente_repo.get_all()
        
        alerts = []
        for cliente in clientes:
            churn_prob = self.ml_service.predict_churn(db, cliente.cliente_id)
            
            if churn_prob > 0.7:
                alerts.append({
                    "tipo": "risco_churn",
                    "severidade": "alta",
                    "mensagem": f"Cliente '{cliente.nome}' com alta probabilidade de cancelamento: {churn_prob*100:.1f}%",
                    "cliente_id": cliente.cliente_id,
                    "produto_id": None
                })
            elif churn_prob > 0.5:
                alerts.append({
                    "tipo": "risco_churn",
                    "severidade": "media",
                    "mensagem": f"Cliente '{cliente.nome}' com probabilidade moderada de cancelamento: {churn_prob*100:.1f}%",
                    "cliente_id": cliente.cliente_id,
                    "produto_id": None
                })
        
        return alerts
