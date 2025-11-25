import random
from typing import List
from sqlalchemy.orm import Session
from app.repositories import ProdutoRepository, CompraRepository


class RecommendationService:
    """Service for product recommendations."""
    
    def get_recommendations(self, db: Session, cliente_id: int, limit: int = 5) -> List[dict]:
        """Get product recommendations for a customer based on purchase history."""
        compra_repo = CompraRepository(db)
        produto_repo = ProdutoRepository(db)
        
        # Get customer preferences
        preferences = compra_repo.get_cliente_produto_preferences(cliente_id)
        tipos_uva_preferidos = preferences['tipos_uva']
        paises_preferidos = preferences['paises']
        produtos_comprados = preferences['produtos_comprados']
        
        # Get all products
        produtos = produto_repo.get_all()
        
        # Score products
        scored_products = []
        for produto in produtos:
            if produto.produto_id in produtos_comprados:
                continue
            
            score = 0
            # Bonus for preferred grape type
            if produto.tipo_uva in tipos_uva_preferidos:
                score += tipos_uva_preferidos[produto.tipo_uva] * 2
            # Bonus for preferred country
            if produto.pais in paises_preferidos:
                score += paises_preferidos[produto.pais] * 1.5
            # Bonus for recent vintages
            if produto.safra >= 2020:
                score += 1
            # Random factor for diversity
            score += random.uniform(0, 1)
            
            scored_products.append({
                "produto_id": produto.produto_id,
                "nome": produto.nome,
                "pais": produto.pais,
                "safra": produto.safra,
                "tipo_uva": produto.tipo_uva,
                "estoque": produto.estoque,
                "preco": float(produto.preco),
                "score": score,
                "motivo": f"Baseado em suas preferencias por {produto.tipo_uva} e vinhos de {produto.pais}"
            })
        
        # Sort by score and return top recommendations
        scored_products.sort(key=lambda x: x['score'], reverse=True)
        return scored_products[:limit]
