from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/api", tags=["dashboard"])


def get_ml_service():
    """Get ML service from app state."""
    from app.main import app
    return app.state.ml_service


def get_alert_service():
    """Get alert service from app state."""
    from app.main import app
    return app.state.alert_service


def get_analytics_service():
    """Get analytics service from app state."""
    from app.main import app
    return app.state.analytics_service


@router.get("/dashboard")
async def get_dashboard(db: Session = Depends(get_db)):
    """Get dashboard summary data."""
    from app.main import app
    alertas = app.state.alertas
    analytics_service = get_analytics_service()
    return analytics_service.get_dashboard_data(db, len(alertas))


@router.get("/alertas")
async def get_alertas():
    """Get strategic alerts."""
    from app.main import app
    return app.state.alertas
