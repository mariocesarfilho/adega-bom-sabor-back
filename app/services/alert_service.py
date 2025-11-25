from typing import List
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.repositories import ClienteRepository, ProdutoRepository, CompraRepository
from app.services.ml_service import MLService
from app.models.compra import Compra


class AlertService:
    """Service for generating strategic alerts using symbolic AI rules.
    
    IA Simbolica - Base de Conhecimento com regras SE-ENTAO:
    - SE cliente > 60 dias sem comprar -> marcar como inativo e sugerir reativacao
    - SE comprou 3 meses seguidos o mesmo tipo de uva -> recomendar semelhantes
    - SE demanda historica aumenta -> alerta estrategico de reposicao (conceitual)
    
    IMPORTANTE: Regras de estoque sao apenas conceituais/simbolicas.
    A base real NAO possui estoque em produtos.
    """
    
    def __init__(self, ml_service: MLService):
        self.ml_service = ml_service
    
    def generate_alerts(self, db: Session) -> List[dict]:
        """Generate all strategic alerts using symbolic AI rules."""
        alerts = []
        
        # Churn risk alerts (ML-based)
        alerts.extend(self._generate_churn_alerts(db))
        
        # Inactive customer alerts (Symbolic AI rule)
        alerts.extend(self._generate_inactivity_alerts(db))
        
        # Loyalty pattern alerts (Symbolic AI rule)
        alerts.extend(self._generate_loyalty_alerts(db))
        
        # Demand trend alerts (Symbolic AI rule - conceptual)
        alerts.extend(self._generate_demand_alerts(db))
        
        return alerts
    
    def _generate_churn_alerts(self, db: Session) -> List[dict]:
        """Generate alerts for customers with high churn risk.
        
        Baseado no modelo de ML treinado com cancelou_assinatura real.
        """
        cliente_repo = ClienteRepository(db)
        clientes = cliente_repo.get_all()
        
        alerts = []
        for cliente in clientes:
            churn_prob = self.ml_service.predict_churn(db, cliente.cliente_id)
            
            if churn_prob > 0.7:
                alerts.append({
                    "tipo": "risco_churn",
                    "severidade": "alta",
                    "mensagem": f"Cliente '{cliente.nome}' com alta probabilidade de cancelamento: {churn_prob*100:.1f}%",
                    "cliente_id": cliente.cliente_id,
                    "produto_id": None,
                    "acao_sugerida": "Contatar cliente com oferta especial de retencao"
                })
            elif churn_prob > 0.5:
                alerts.append({
                    "tipo": "risco_churn",
                    "severidade": "media",
                    "mensagem": f"Cliente '{cliente.nome}' com probabilidade moderada de cancelamento: {churn_prob*100:.1f}%",
                    "cliente_id": cliente.cliente_id,
                    "produto_id": None,
                    "acao_sugerida": "Enviar comunicacao de engajamento"
                })
        
        return alerts
    
    def _generate_inactivity_alerts(self, db: Session) -> List[dict]:
        """Generate alerts for inactive customers.
        
        Regra simbolica: SE cliente > 60 dias sem comprar -> marcar como inativo e sugerir reativacao
        """
        cliente_repo = ClienteRepository(db)
        inativos = cliente_repo.get_inativos(dias_limite=60)
        
        alerts = []
        for cliente in inativos:
            alerts.append({
                "tipo": "cliente_inativo",
                "severidade": "media",
                "mensagem": f"Cliente '{cliente.nome}' esta ha mais de 60 dias sem comprar",
                "cliente_id": cliente.cliente_id,
                "produto_id": None,
                "acao_sugerida": "Enviar campanha de reativacao com desconto especial"
            })
        
        return alerts
    
    def _generate_loyalty_alerts(self, db: Session) -> List[dict]:
        """Generate alerts for loyal customers with consistent preferences.
        
        Regra simbolica: SE comprou 3 meses seguidos o mesmo tipo de uva -> recomendar semelhantes
        """
        alerts = []
        
        # Get customers with consistent grape type preferences
        cliente_repo = ClienteRepository(db)
        clientes = cliente_repo.get_all()
        
        for cliente in clientes:
            # Check if customer has bought same grape type in last 3 months
            loyalty_pattern = self._check_grape_loyalty(db, cliente.cliente_id)
            if loyalty_pattern:
                alerts.append({
                    "tipo": "fidelidade_uva",
                    "severidade": "baixa",
                    "mensagem": f"Cliente '{cliente.nome}' comprou {loyalty_pattern['tipo_uva']} nos ultimos 3 meses",
                    "cliente_id": cliente.cliente_id,
                    "produto_id": None,
                    "acao_sugerida": f"Recomendar outros vinhos {loyalty_pattern['tipo_uva']} ou similares"
                })
        
        return alerts
    
    def _check_grape_loyalty(self, db: Session, cliente_id: int) -> dict:
        """Check if customer has consistent grape type preference in last 3 months."""
        from app.models.produto import Produto
        
        three_months_ago = datetime.now().date() - timedelta(days=90)
        
        # Get grape types purchased in last 3 months
        result = db.query(
            Produto.tipo_uva,
            func.count(Compra.compra_id).label('count')
        ).join(Compra, Produto.produto_id == Compra.produto_id
        ).filter(
            Compra.cliente_id == cliente_id,
            Compra.data_compra >= three_months_ago
        ).group_by(Produto.tipo_uva).all()
        
        if not result:
            return None
        
        # Check if there's a dominant grape type (more than 50% of purchases)
        total = sum(r.count for r in result)
        for r in result:
            if r.count >= 3 and r.count / total >= 0.5:
                return {"tipo_uva": r.tipo_uva, "count": r.count}
        
        return None
    
    def _generate_demand_alerts(self, db: Session) -> List[dict]:
        """Generate conceptual demand alerts.
        
        Regra simbolica (CONCEITUAL): SE demanda historica aumenta -> alerta estrategico de reposicao
        
        IMPORTANTE: Esta regra e apenas conceitual/simbolica.
        A base real NAO possui estoque em produtos.
        Os alertas sao baseados em tendencias de demanda, nao em niveis de estoque.
        """
        alerts = []
        
        # Analyze demand trends for products
        from app.models.produto import Produto
        
        # Get products with increasing demand (more purchases in last 30 days vs previous 30 days)
        thirty_days_ago = datetime.now().date() - timedelta(days=30)
        sixty_days_ago = datetime.now().date() - timedelta(days=60)
        
        # Recent period purchases
        recent = db.query(
            Compra.produto_id,
            func.sum(Compra.quantidade).label('qtd_recente')
        ).filter(
            Compra.data_compra >= thirty_days_ago
        ).group_by(Compra.produto_id).subquery()
        
        # Previous period purchases
        previous = db.query(
            Compra.produto_id,
            func.sum(Compra.quantidade).label('qtd_anterior')
        ).filter(
            Compra.data_compra >= sixty_days_ago,
            Compra.data_compra < thirty_days_ago
        ).group_by(Compra.produto_id).subquery()
        
        # Find products with significant demand increase
        result = db.query(
            Produto.produto_id,
            Produto.nome,
            recent.c.qtd_recente,
            previous.c.qtd_anterior
        ).outerjoin(recent, Produto.produto_id == recent.c.produto_id
        ).outerjoin(previous, Produto.produto_id == previous.c.produto_id
        ).filter(
            recent.c.qtd_recente != None,
            previous.c.qtd_anterior != None
        ).all()
        
        for r in result:
            if r.qtd_recente and r.qtd_anterior:
                if r.qtd_recente > r.qtd_anterior * 1.5:  # 50% increase
                    alerts.append({
                        "tipo": "demanda_crescente",
                        "severidade": "baixa",
                        "mensagem": f"Produto '{r.nome}' com demanda crescente: {r.qtd_anterior} -> {r.qtd_recente} unidades",
                        "cliente_id": None,
                        "produto_id": r.produto_id,
                        "acao_sugerida": "Considerar reposicao estrategica (alerta conceitual)"
                    })
        
        return alerts
