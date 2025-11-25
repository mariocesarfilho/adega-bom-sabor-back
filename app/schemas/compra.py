from pydantic import BaseModel
from decimal import Decimal
from datetime import date
from typing import Optional


class CompraBase(BaseModel):
    """Base schema for purchase data."""
    cliente_id: int
    produto_id: int
    valor: Decimal
    quantidade: int
    data_compra: date


class CompraCreate(CompraBase):
    """Schema for creating a purchase."""
    compra_id: int


class CompraResponse(CompraBase):
    """Schema for purchase response."""
    compra_id: int
    
    class Config:
        from_attributes = True


class CompraWithDetails(CompraResponse):
    """Schema for purchase with client and product names."""
    cliente_nome: str
    produto_nome: str


class VendasPorMes(BaseModel):
    """Schema for sales by month."""
    mes: str
    valor: float
    quantidade: int
