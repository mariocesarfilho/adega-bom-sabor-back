from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import get_settings
from app.database import engine, Base, SessionLocal
from app.services import MLService, RecommendationService, AlertService, AnalyticsService
from app.routes import (
    dashboard_router, 
    clientes_router, 
    produtos_router, 
    compras_router, 
    analytics_router
)

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup and shutdown events."""
    # Startup
    print("Starting application...")
    
    # Initialize services
    app.state.ml_service = MLService()
    app.state.recommendation_service = RecommendationService()
    app.state.alert_service = AlertService(app.state.ml_service)
    app.state.analytics_service = AnalyticsService(app.state.ml_service)
    app.state.alertas = []
    
    # Train ML models
    db = SessionLocal()
    try:
        success = app.state.ml_service.train_models(db)
        if success:
            # Generate alerts after training
            app.state.alertas = app.state.alert_service.generate_alerts(db)
            print(f"Generated {len(app.state.alertas)} alerts")
        else:
            print("Warning: ML models could not be trained. Check if database has data.")
    finally:
        db.close()
    
    print("Application started successfully")
    
    yield
    
    # Shutdown
    print("Shutting down application...")


app = FastAPI(
    title=settings.app_name,
    description="Sistema de Apoio a Decisao para gestao de adega com ML",
    version="2.0.0",
    lifespan=lifespan
)

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(dashboard_router)
app.include_router(clientes_router)
app.include_router(produtos_router)
app.include_router(compras_router)
app.include_router(analytics_router)


@app.get("/healthz")
async def healthz():
    """Health check endpoint."""
    return {"status": "ok"}


@app.post("/api/ml/retrain")
async def retrain_models():
    """Retrain ML models with current database data."""
    db = SessionLocal()
    try:
        success = app.state.ml_service.train_models(db)
        if success:
            app.state.alertas = app.state.alert_service.generate_alerts(db)
            return {
                "status": "success", 
                "message": "Modelos retreinados com sucesso",
                "alertas_count": len(app.state.alertas)
            }
        else:
            return {"status": "error", "message": "Falha ao retreinar modelos"}
    finally:
        db.close()
