from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db

router = APIRouter(prefix="/api/analytics", tags=["analytics"])


def get_analytics_service():
    """Get analytics service from app state."""
    from app.main import app
    return app.state.analytics_service


@router.get("/vendas-por-mes")
async def get_vendas_por_mes(db: Session = Depends(get_db)):
    """Get sales by month."""
    analytics_service = get_analytics_service()
    return analytics_service.get_vendas_por_mes(db)


@router.get("/top-produtos")
async def get_top_produtos(db: Session = Depends(get_db)):
    """Get top selling products."""
    analytics_service = get_analytics_service()
    return analytics_service.get_top_produtos(db)


@router.get("/clientes-por-cidade")
async def get_clientes_por_cidade(db: Session = Depends(get_db)):
    """Get customers by city."""
    analytics_service = get_analytics_service()
    return analytics_service.get_clientes_por_cidade(db)
