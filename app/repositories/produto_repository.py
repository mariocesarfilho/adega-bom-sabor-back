from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from app.models.produto import Produto


class ProdutoRepository:
    """Repository for product data access.
    
    IMPORTANTE: A base real NAO possui preco nem estoque em produtos.
    O preco esta na tabela de compras (valor da transacao).
    """
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> List[Produto]:
        """Get all products."""
        return self.db.query(Produto).all()
    
    def get_by_id(self, produto_id: int) -> Optional[Produto]:
        """Get product by ID."""
        return self.db.query(Produto).filter(Produto.produto_id == produto_id).first()
    
    def get_count(self) -> int:
        """Get total number of products."""
        return self.db.query(func.count(Produto.produto_id)).scalar()
    
    def get_by_tipo_uva(self, tipo_uva: str) -> List[Produto]:
        """Get products by grape type."""
        return self.db.query(Produto).filter(Produto.tipo_uva == tipo_uva).all()
    
    def get_by_pais(self, pais: str) -> List[Produto]:
        """Get products by country."""
        return self.db.query(Produto).filter(Produto.pais == pais).all()
    
    def get_by_safra(self, safra: int) -> List[Produto]:
        """Get products by vintage year."""
        return self.db.query(Produto).filter(Produto.safra == safra).all()
    
    def get_distinct_tipos_uva(self) -> List[str]:
        """Get all distinct grape types."""
        result = self.db.query(Produto.tipo_uva).distinct().all()
        return [r[0] for r in result]
    
    def get_distinct_paises(self) -> List[str]:
        """Get all distinct countries."""
        result = self.db.query(Produto.pais).distinct().all()
        return [r[0] for r in result]
