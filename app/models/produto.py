from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from app.database import Base


class Produto(Base):
    """SQLAlchemy model for products (wines)."""
    
    __tablename__ = "produtos"
    
    produto_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    pais = Column(String(100), nullable=False)
    safra = Column(Integer, nullable=False)
    tipo_uva = Column(String(100), nullable=False)
    estoque = Column(Integer, nullable=False, default=50)
    preco = Column(Numeric(10, 2), nullable=False, default=100.00)
    
    # Relationships
    compras = relationship("Compra", back_populates="produto")
    
    def __repr__(self):
        return f"<Produto(id={self.produto_id}, nome='{self.nome}')>"
