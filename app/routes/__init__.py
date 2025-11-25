from app.routes.dashboard import router as dashboard_router
from app.routes.clientes import router as clientes_router
from app.routes.produtos import router as produtos_router
from app.routes.compras import router as compras_router
from app.routes.analytics import router as analytics_router

__all__ = [
    "dashboard_router", 
    "clientes_router", 
    "produtos_router", 
    "compras_router", 
    "analytics_router"
]
