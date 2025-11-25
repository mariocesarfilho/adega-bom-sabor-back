from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.repositories import ProdutoRepository

router = APIRouter(prefix="/api", tags=["produtos"])


@router.get("/produtos")
async def get_produtos(db: Session = Depends(get_db)):
    """Get all products.
    
    IMPORTANTE: A base real NAO possui preco nem estoque em produtos.
    O preco esta na tabela de compras (valor da transacao).
    """
    produto_repo = ProdutoRepository(db)
    produtos = produto_repo.get_all()
    
    return [
        {
            "produto_id": p.produto_id,
            "nome": p.nome,
            "pais": p.pais,
            "safra": p.safra,
            "tipo_uva": p.tipo_uva
        }
        for p in produtos
    ]


@router.get("/produtos/{produto_id}")
async def get_produto(produto_id: int, db: Session = Depends(get_db)):
    """Get product by ID."""
    produto_repo = ProdutoRepository(db)
    produto = produto_repo.get_by_id(produto_id)
    
    if not produto:
        return {"error": "Produto nao encontrado"}
    
    return {
        "produto_id": produto.produto_id,
        "nome": produto.nome,
        "pais": produto.pais,
        "safra": produto.safra,
        "tipo_uva": produto.tipo_uva
    }


@router.get("/produtos/tipos-uva")
async def get_tipos_uva(db: Session = Depends(get_db)):
    """Get all distinct grape types."""
    produto_repo = ProdutoRepository(db)
    return produto_repo.get_distinct_tipos_uva()


@router.get("/produtos/paises")
async def get_paises(db: Session = Depends(get_db)):
    """Get all distinct countries."""
    produto_repo = ProdutoRepository(db)
    return produto_repo.get_distinct_paises()
