from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Produto(Base):
    """SQLAlchemy model for products (wines).
    
    Estrutura baseada na planilha produtos.xlsx.
    IMPORTANTE: A base real NAO possui preco nem estoque em produtos.
    O preco esta na tabela de compras (valor da transacao).
    """
    
    __tablename__ = "produtos"
    
    produto_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    pais = Column(String(100), nullable=False)
    safra = Column(Integer, nullable=False)
    tipo_uva = Column(String(100), nullable=False)
    
    # Relationships
    compras = relationship("Compra", back_populates="produto")
    
    def __repr__(self):
        return f"<Produto(id={self.produto_id}, nome='{self.nome}')>"
