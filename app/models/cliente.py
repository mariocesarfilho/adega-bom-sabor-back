from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Cliente(Base):
    """SQLAlchemy model for customers."""
    
    __tablename__ = "clientes"
    
    cliente_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    idade = Column(Integer, nullable=False)
    cidade = Column(String(100), nullable=False)
    pontuacao_engajamento = Column(Float, nullable=False)
    assinante_clube = Column(Boolean, default=False)
    
    # Relationships
    compras = relationship("Compra", back_populates="cliente")
    
    def __repr__(self):
        return f"<Cliente(id={self.cliente_id}, nome='{self.nome}')>"
