from pydantic import BaseModel
from decimal import Decimal
from typing import Optional


class ProdutoBase(BaseModel):
    """Base schema for product data."""
    nome: str
    pais: str
    safra: int
    tipo_uva: str
    estoque: int
    preco: Decimal


class ProdutoCreate(ProdutoBase):
    """Schema for creating a product."""
    produto_id: int


class ProdutoResponse(ProdutoBase):
    """Schema for product response."""
    produto_id: int
    
    class Config:
        from_attributes = True


class ProdutoRecomendacao(ProdutoResponse):
    """Schema for product recommendation."""
    score: float
    motivo: str


class TopProduto(BaseModel):
    """Schema for top selling product."""
    produto_id: int
    nome: str
    quantidade_vendida: int
    valor_total: float
