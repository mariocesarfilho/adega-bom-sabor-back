from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.repositories import CompraRepository

router = APIRouter(prefix="/api", tags=["compras"])


@router.get("/compras")
async def get_compras(db: Session = Depends(get_db)):
    """Get all purchases with client and product names."""
    compra_repo = CompraRepository(db)
    return compra_repo.get_all_with_details()
