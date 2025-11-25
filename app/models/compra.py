from sqlalchemy import Column, Integer, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Compra(Base):
    """SQLAlchemy model for purchases."""
    
    __tablename__ = "compras"
    
    compra_id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.cliente_id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.produto_id"), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    quantidade = Column(Integer, nullable=False)
    data_compra = Column(Date, nullable=False)
    
    # Relationships
    cliente = relationship("Cliente", back_populates="compras")
    produto = relationship("Produto", back_populates="compras")
    
    def __repr__(self):
        return f"<Compra(id={self.compra_id}, cliente_id={self.cliente_id}, produto_id={self.produto_id})>"
