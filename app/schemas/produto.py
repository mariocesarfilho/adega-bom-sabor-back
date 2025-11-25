from pydantic import BaseModel
from typing import Optional


class ProdutoBase(BaseModel):
    """Base schema for product data.
    
    Estrutura baseada na planilha produtos.xlsx.
    IMPORTANTE: A base real NAO possui preco nem estoque em produtos.
    O preco esta na tabela de compras (valor da transacao).
    """
    nome: str
    pais: str
    safra: int
    tipo_uva: str


class ProdutoCreate(ProdutoBase):
    """Schema for creating a product."""
    produto_id: int


class ProdutoResponse(ProdutoBase):
    """Schema for product response."""
    produto_id: int
    
    class Config:
        from_attributes = True


class ProdutoRecomendacao(BaseModel):
    """Schema for product recommendation.
    
    Recomendacao baseada em filtragem por conteudo (tipo_uva, pais, safra).
    """
    produto_id: int
    nome: str
    pais: str
    safra: int
    tipo_uva: str
    score: float
    motivo: str


class TopProduto(BaseModel):
    """Schema for top selling product."""
    produto_id: int
    nome: str
    quantidade_vendida: int
    valor_total: float
