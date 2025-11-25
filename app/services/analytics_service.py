from typing import List, Dict
from sqlalchemy.orm import Session
from app.repositories import ClienteRepository, ProdutoRepository, CompraRepository
from app.services.ml_service import MLService


class AnalyticsService:
    """Service for analytics and dashboard data."""
    
    def __init__(self, ml_service: MLService):
        self.ml_service = ml_service
    
    def get_dashboard_data(self, db: Session, alertas_count: int) -> dict:
        """Get dashboard summary data."""
        cliente_repo = ClienteRepository(db)
        produto_repo = ProdutoRepository(db)
        compra_repo = CompraRepository(db)
        
        total_clientes = cliente_repo.get_count()
        total_produtos = produto_repo.get_count()
        total_compras = compra_repo.get_count()
        valor_total_vendas = compra_repo.get_total_valor()
        
        # Churn distribution
        churn_alto = 0
        churn_medio = 0
        churn_baixo = 0
        
        clientes = cliente_repo.get_all()
        for cliente in clientes:
            prob = self.ml_service.predict_churn(db, cliente.cliente_id)
            if prob > 0.7:
                churn_alto += 1
            elif prob > 0.4:
                churn_medio += 1
            else:
                churn_baixo += 1
        
        # Segment distribution
        segmentos = {"Premium": 0, "Sensivel a Promocoes": 0, "Ocasional": 0}
        for cliente in clientes:
            seg = self.ml_service.predict_segment(db, cliente.cliente_id)
            if seg['segmento'] in segmentos:
                segmentos[seg['segmento']] += 1
        
        return {
            "total_clientes": total_clientes,
            "total_produtos": total_produtos,
            "total_compras": total_compras,
            "valor_total_vendas": round(valor_total_vendas, 2),
            "churn_distribution": {
                "alto": churn_alto,
                "medio": churn_medio,
                "baixo": churn_baixo
            },
            "segment_distribution": segmentos,
            "alertas_count": alertas_count
        }
    
    def get_churn_analysis(self, db: Session) -> List[dict]:
        """Get churn analysis for all customers."""
        cliente_repo = ClienteRepository(db)
        clientes = cliente_repo.get_all()
        
        result = []
        for cliente in clientes:
            prob = self.ml_service.predict_churn(db, cliente.cliente_id)
            result.append({
                "cliente_id": cliente.cliente_id,
                "nome": cliente.nome,
                "churn_probability": round(prob, 2),
                "risco": "Alto" if prob > 0.7 else ("Medio" if prob > 0.4 else "Baixo")
            })
        
        result.sort(key=lambda x: x['churn_probability'], reverse=True)
        return result
    
    def get_segmentation(self, db: Session) -> List[dict]:
        """Get customer segmentation data."""
        cliente_repo = ClienteRepository(db)
        compra_repo = CompraRepository(db)
        clientes = cliente_repo.get_all()
        
        result = []
        for cliente in clientes:
            segment = self.ml_service.predict_segment(db, cliente.cliente_id)
            compras = compra_repo.get_by_cliente(cliente.cliente_id)
            total_gasto = sum(float(c.valor) * c.quantidade for c in compras)
            
            result.append({
                "cliente_id": cliente.cliente_id,
                "nome": cliente.nome,
                "segmento": segment['segmento'],
                "descricao": segment['descricao'],
                "total_compras": len(compras),
                "total_gasto": round(total_gasto, 2)
            })
        
        return result
    
    def get_vendas_por_mes(self, db: Session) -> List[dict]:
        """Get sales by month."""
        compra_repo = CompraRepository(db)
        return compra_repo.get_vendas_por_mes()
    
    def get_top_produtos(self, db: Session, limit: int = 10) -> List[dict]:
        """Get top selling products."""
        compra_repo = CompraRepository(db)
        return compra_repo.get_top_produtos(limit)
    
    def get_clientes_por_cidade(self, db: Session) -> List[dict]:
        """Get customers by city."""
        cliente_repo = ClienteRepository(db)
        return cliente_repo.get_by_cidade()
