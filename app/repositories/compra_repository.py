from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from typing import List, Optional
from datetime import date
from app.models.compra import Compra
from app.models.cliente import Cliente
from app.models.produto import Produto


class CompraRepository:
    """Repository for purchase data access."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> List[Compra]:
        """Get all purchases."""
        return self.db.query(Compra).all()
    
    def get_by_id(self, compra_id: int) -> Optional[Compra]:
        """Get purchase by ID."""
        return self.db.query(Compra).filter(Compra.compra_id == compra_id).first()
    
    def get_count(self) -> int:
        """Get total number of purchases."""
        return self.db.query(func.count(Compra.compra_id)).scalar()
    
    def get_by_cliente(self, cliente_id: int) -> List[Compra]:
        """Get purchases by customer ID."""
        return self.db.query(Compra).filter(Compra.cliente_id == cliente_id).all()
    
    def get_total_valor(self) -> float:
        """Get total sales value."""
        result = self.db.query(
            func.sum(Compra.valor * Compra.quantidade)
        ).scalar()
        return float(result or 0)
    
    def get_vendas_por_mes(self) -> List[dict]:
        """Get sales aggregated by month."""
        result = self.db.query(
            func.to_char(Compra.data_compra, 'YYYY-MM').label('mes'),
            func.sum(Compra.valor * Compra.quantidade).label('valor'),
            func.sum(Compra.quantidade).label('quantidade')
        ).group_by(
            func.to_char(Compra.data_compra, 'YYYY-MM')
        ).order_by('mes').all()
        
        return [
            {"mes": r.mes, "valor": float(r.valor or 0), "quantidade": int(r.quantidade or 0)}
            for r in result
        ]
    
    def get_top_produtos(self, limit: int = 10) -> List[dict]:
        """Get top selling products."""
        result = self.db.query(
            Compra.produto_id,
            Produto.nome,
            func.sum(Compra.quantidade).label('quantidade_vendida'),
            func.sum(Compra.valor * Compra.quantidade).label('valor_total')
        ).join(
            Produto, Compra.produto_id == Produto.produto_id
        ).group_by(
            Compra.produto_id, Produto.nome
        ).order_by(
            func.sum(Compra.valor * Compra.quantidade).desc()
        ).limit(limit).all()
        
        return [
            {
                "produto_id": r.produto_id,
                "nome": r.nome,
                "quantidade_vendida": int(r.quantidade_vendida or 0),
                "valor_total": float(r.valor_total or 0)
            }
            for r in result
        ]
    
    def get_cliente_compras_with_details(self, cliente_id: int) -> List[dict]:
        """Get customer purchases with product details."""
        result = self.db.query(
            Compra, Produto.nome.label('produto_nome')
        ).join(
            Produto, Compra.produto_id == Produto.produto_id
        ).filter(
            Compra.cliente_id == cliente_id
        ).all()
        
        return [
            {
                "compra_id": r.Compra.compra_id,
                "cliente_id": r.Compra.cliente_id,
                "produto_id": r.Compra.produto_id,
                "valor": float(r.Compra.valor),
                "quantidade": r.Compra.quantidade,
                "data_compra": str(r.Compra.data_compra),
                "produto_nome": r.produto_nome
            }
            for r in result
        ]
    
    def get_all_with_details(self) -> List[dict]:
        """Get all purchases with client and product names."""
        result = self.db.query(
            Compra,
            Cliente.nome.label('cliente_nome'),
            Produto.nome.label('produto_nome')
        ).join(
            Cliente, Compra.cliente_id == Cliente.cliente_id
        ).join(
            Produto, Compra.produto_id == Produto.produto_id
        ).all()
        
        return [
            {
                "compra_id": r.Compra.compra_id,
                "cliente_id": r.Compra.cliente_id,
                "produto_id": r.Compra.produto_id,
                "valor": float(r.Compra.valor),
                "quantidade": r.Compra.quantidade,
                "data_compra": str(r.Compra.data_compra),
                "cliente_nome": r.cliente_nome,
                "produto_nome": r.produto_nome
            }
            for r in result
        ]
    
    def get_cliente_produto_preferences(self, cliente_id: int) -> dict:
        """Get customer's product preferences (grape types and countries)."""
        result = self.db.query(
            Produto.tipo_uva,
            Produto.pais,
            func.count(Compra.compra_id).label('count')
        ).join(
            Produto, Compra.produto_id == Produto.produto_id
        ).filter(
            Compra.cliente_id == cliente_id
        ).group_by(
            Produto.tipo_uva, Produto.pais
        ).all()
        
        tipos_uva = {}
        paises = {}
        produtos_comprados = set()
        
        for r in result:
            tipos_uva[r.tipo_uva] = tipos_uva.get(r.tipo_uva, 0) + r.count
            paises[r.pais] = paises.get(r.pais, 0) + r.count
        
        # Get purchased product IDs
        compras = self.get_by_cliente(cliente_id)
        produtos_comprados = {c.produto_id for c in compras}
        
        return {
            "tipos_uva": tipos_uva,
            "paises": paises,
            "produtos_comprados": produtos_comprados
        }
