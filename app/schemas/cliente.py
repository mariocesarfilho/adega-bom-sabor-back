from pydantic import BaseModel
from typing import Optional, List


class ClienteBase(BaseModel):
    """Base schema for customer data."""
    nome: str
    idade: int
    cidade: str
    pontuacao_engajamento: float
    assinante_clube: bool


class ClienteCreate(ClienteBase):
    """Schema for creating a customer."""
    cliente_id: int


class ClienteResponse(ClienteBase):
    """Schema for customer response."""
    cliente_id: int
    
    class Config:
        from_attributes = True


class ClienteWithAnalytics(ClienteResponse):
    """Schema for customer with churn and segmentation data."""
    churn_probability: float
    segmento: str
    segmento_descricao: str
    total_compras: int
    total_gasto: float


class ClienteDetalhes(ClienteWithAnalytics):
    """Schema for detailed customer view with recommendations."""
    recomendacoes: List[dict]
    historico_compras: List[dict]


class ChurnAnalysis(BaseModel):
    """Schema for churn analysis response."""
    cliente_id: int
    nome: str
    churn_probability: float
    risco: str


class SegmentacaoResponse(BaseModel):
    """Schema for segmentation response."""
    cliente_id: int
    nome: str
    segmento: str
    descricao: str
    total_compras: int
    total_gasto: float
