from pydantic import BaseModel
from typing import Dict


class ChurnDistribution(BaseModel):
    """Schema for churn distribution."""
    alto: int
    medio: int
    baixo: int


class DashboardResponse(BaseModel):
    """Schema for dashboard summary response."""
    total_clientes: int
    total_produtos: int
    total_compras: int
    valor_total_vendas: float
    churn_distribution: ChurnDistribution
    segment_distribution: Dict[str, int]
    alertas_count: int


class AlertaResponse(BaseModel):
    """Schema for alert response."""
    tipo: str
    severidade: str
    mensagem: str
    produto_id: int = None
    cliente_id: int = None


class CidadeCount(BaseModel):
    """Schema for customers by city."""
    cidade: str
    quantidade: int
