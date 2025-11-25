from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.repositories import ProdutoRepository

router = APIRouter(prefix="/api", tags=["produtos"])


@router.get("/produtos")
async def get_produtos(db: Session = Depends(get_db)):
    """Get all products."""
    produto_repo = ProdutoRepository(db)
    produtos = produto_repo.get_all()
    
    return [
        {
            "produto_id": p.produto_id,
            "nome": p.nome,
            "pais": p.pais,
            "safra": p.safra,
            "tipo_uva": p.tipo_uva,
            "estoque": p.estoque,
            "preco": float(p.preco)
        }
        for p in produtos
    ]
