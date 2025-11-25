from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from app.models.produto import Produto


class ProdutoRepository:
    """Repository for product data access."""
    
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
    
    def get_low_stock(self, threshold: int = 20) -> List[Produto]:
        """Get products with low stock."""
        return self.db.query(Produto).filter(Produto.estoque < threshold).all()
    
    def get_by_tipo_uva(self, tipo_uva: str) -> List[Produto]:
        """Get products by grape type."""
        return self.db.query(Produto).filter(Produto.tipo_uva == tipo_uva).all()
    
    def get_by_pais(self, pais: str) -> List[Produto]:
        """Get products by country."""
        return self.db.query(Produto).filter(Produto.pais == pais).all()
