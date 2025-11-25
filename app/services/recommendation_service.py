import random
from typing import List
from sqlalchemy.orm import Session
from app.repositories import ProdutoRepository, CompraRepository


class RecommendationService:
    """Service for product recommendations using content-based filtering.
    
    Sistema de Recomendacao baseado em filtragem por conteudo:
    - Usa atributos do produto: tipo_uva, safra, pais
    - Recomenda produtos similares com base no historico de compras
    
    IMPORTANTE: A base real NAO possui preco nem estoque em produtos.
    """
    
    def get_recommendations(self, db: Session, cliente_id: int, limit: int = 5) -> List[dict]:
        """Get product recommendations for a customer based on purchase history.
        
        Filtragem baseada em conteudo usando:
        - tipo_uva preferido
        - pais preferido
        - safra (bonus para safras recentes)
        """
        compra_repo = CompraRepository(db)
        produto_repo = ProdutoRepository(db)
        
        # Get customer preferences
        preferences = compra_repo.get_cliente_produto_preferences(cliente_id)
        tipos_uva_preferidos = preferences['tipos_uva']
        paises_preferidos = preferences['paises']
        produtos_comprados = preferences['produtos_comprados']
        
        # Get all products
        produtos = produto_repo.get_all()
        
        # Score products based on content similarity
        scored_products = []
        for produto in produtos:
            if produto.produto_id in produtos_comprados:
                continue
            
            score = 0
            motivos = []
            
            # Bonus for preferred grape type (content-based filtering)
            if produto.tipo_uva in tipos_uva_preferidos:
                score += tipos_uva_preferidos[produto.tipo_uva] * 2
                motivos.append(f"voce gosta de {produto.tipo_uva}")
            
            # Bonus for preferred country (content-based filtering)
            if produto.pais in paises_preferidos:
                score += paises_preferidos[produto.pais] * 1.5
                motivos.append(f"vinhos de {produto.pais}")
            
            # Bonus for recent vintages
            if produto.safra >= 2020:
                score += 1
                motivos.append(f"safra recente ({produto.safra})")
            
            # Random factor for diversity
            score += random.uniform(0, 1)
            
            # Build recommendation reason
            if motivos:
                motivo = f"Recomendado porque {', '.join(motivos)}"
            else:
                motivo = "Sugestao para diversificar suas escolhas"
            
            scored_products.append({
                "produto_id": produto.produto_id,
                "nome": produto.nome,
                "pais": produto.pais,
                "safra": produto.safra,
                "tipo_uva": produto.tipo_uva,
                "score": score,
                "motivo": motivo
            })
        
        # Sort by score and return top recommendations
        scored_products.sort(key=lambda x: x['score'], reverse=True)
        return scored_products[:limit]
    
    def get_similar_products(self, db: Session, produto_id: int, limit: int = 5) -> List[dict]:
        """Get products similar to a given product based on content attributes.
        
        Regra simbolica: SE comprou 3 meses seguidos o mesmo tipo de uva -> recomendar semelhantes
        """
        produto_repo = ProdutoRepository(db)
        
        produto = produto_repo.get_by_id(produto_id)
        if not produto:
            return []
        
        # Get products with same grape type or country
        all_produtos = produto_repo.get_all()
        
        similar = []
        for p in all_produtos:
            if p.produto_id == produto_id:
                continue
            
            score = 0
            motivos = []
            
            # Same grape type
            if p.tipo_uva == produto.tipo_uva:
                score += 3
                motivos.append(f"mesmo tipo de uva ({p.tipo_uva})")
            
            # Same country
            if p.pais == produto.pais:
                score += 2
                motivos.append(f"mesmo pais ({p.pais})")
            
            # Similar vintage
            if abs(p.safra - produto.safra) <= 2:
                score += 1
                motivos.append("safra similar")
            
            if score > 0:
                similar.append({
                    "produto_id": p.produto_id,
                    "nome": p.nome,
                    "pais": p.pais,
                    "safra": p.safra,
                    "tipo_uva": p.tipo_uva,
                    "score": score,
                    "motivo": f"Similar porque: {', '.join(motivos)}"
                })
        
        similar.sort(key=lambda x: x['score'], reverse=True)
        return similar[:limit]
