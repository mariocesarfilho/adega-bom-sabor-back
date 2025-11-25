from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.repositories import ClienteRepository, CompraRepository

router = APIRouter(prefix="/api", tags=["clientes"])


def get_ml_service():
    """Get ML service from app state."""
    from app.main import app
    return app.state.ml_service


def get_recommendation_service():
    """Get recommendation service from app state."""
    from app.main import app
    return app.state.recommendation_service


@router.get("/clientes")
async def get_clientes(db: Session = Depends(get_db)):
    """Get all customers with churn probability and segment."""
    ml_service = get_ml_service()
    cliente_repo = ClienteRepository(db)
    compra_repo = CompraRepository(db)
    
    clientes = cliente_repo.get_all()
    result = []
    
    for cliente in clientes:
        churn_prob = ml_service.predict_churn(db, cliente.cliente_id)
        segment = ml_service.predict_segment(db, cliente.cliente_id)
        
        compras = compra_repo.get_by_cliente(cliente.cliente_id)
        total_gasto = sum(float(c.valor) * c.quantidade for c in compras)
        
        result.append({
            "cliente_id": cliente.cliente_id,
            "nome": cliente.nome,
            "idade": cliente.idade,
            "cidade": cliente.cidade,
            "pontuacao_engajamento": cliente.pontuacao_engajamento,
            "assinante_clube": cliente.assinante_clube,
            "churn_probability": round(churn_prob, 2),
            "segmento": segment['segmento'],
            "segmento_descricao": segment['descricao'],
            "total_compras": len(compras),
            "total_gasto": round(total_gasto, 2)
        })
    
    return result


@router.get("/clientes/{cliente_id}")
async def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    """Get customer details with recommendations."""
    ml_service = get_ml_service()
    recommendation_service = get_recommendation_service()
    cliente_repo = ClienteRepository(db)
    compra_repo = CompraRepository(db)
    
    cliente = cliente_repo.get_by_id(cliente_id)
    if not cliente:
        return {"error": "Cliente nao encontrado"}
    
    churn_prob = ml_service.predict_churn(db, cliente_id)
    segment = ml_service.predict_segment(db, cliente_id)
    recommendations = recommendation_service.get_recommendations(db, cliente_id)
    historico = compra_repo.get_cliente_compras_with_details(cliente_id)
    
    return {
        "cliente_id": cliente.cliente_id,
        "nome": cliente.nome,
        "idade": cliente.idade,
        "cidade": cliente.cidade,
        "pontuacao_engajamento": cliente.pontuacao_engajamento,
        "assinante_clube": cliente.assinante_clube,
        "churn_probability": round(churn_prob, 2),
        "segmento": segment['segmento'],
        "segmento_descricao": segment['descricao'],
        "recomendacoes": recommendations,
        "historico_compras": historico
    }


@router.get("/churn")
async def get_churn_analysis(db: Session = Depends(get_db)):
    """Get churn analysis for all customers."""
    from app.main import app
    analytics_service = app.state.analytics_service
    return analytics_service.get_churn_analysis(db)


@router.get("/segmentacao")
async def get_segmentacao(db: Session = Depends(get_db)):
    """Get customer segmentation."""
    from app.main import app
    analytics_service = app.state.analytics_service
    return analytics_service.get_segmentation(db)


@router.get("/recomendacoes/{cliente_id}")
async def get_recomendacoes(cliente_id: int, limit: int = 5, db: Session = Depends(get_db)):
    """Get product recommendations for a customer."""
    recommendation_service = get_recommendation_service()
    return recommendation_service.get_recommendations(db, cliente_id, limit)
