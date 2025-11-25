from app.schemas.cliente import (
    ClienteBase, ClienteCreate, ClienteResponse, 
    ClienteWithAnalytics, ClienteDetalhes, ChurnAnalysis, SegmentacaoResponse
)
from app.schemas.produto import (
    ProdutoBase, ProdutoCreate, ProdutoResponse, 
    ProdutoRecomendacao, TopProduto
)
from app.schemas.compra import (
    CompraBase, CompraCreate, CompraResponse, 
    CompraWithDetails, VendasPorMes
)
from app.schemas.dashboard import (
    ChurnDistribution, DashboardResponse, AlertaResponse, CidadeCount
)

__all__ = [
    "ClienteBase", "ClienteCreate", "ClienteResponse", 
    "ClienteWithAnalytics", "ClienteDetalhes", "ChurnAnalysis", "SegmentacaoResponse",
    "ProdutoBase", "ProdutoCreate", "ProdutoResponse", 
    "ProdutoRecomendacao", "TopProduto",
    "CompraBase", "CompraCreate", "CompraResponse", 
    "CompraWithDetails", "VendasPorMes",
    "ChurnDistribution", "DashboardResponse", "AlertaResponse", "CidadeCount"
]
