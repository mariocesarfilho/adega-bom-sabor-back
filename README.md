# Adega Bom Sabor - Backend API

API FastAPI para o Sistema de Apoio a Decisao (SAD) da Adega Bom Sabor.

## Funcionalidades

- Previsao de Churn com Random Forest
- Segmentacao de Clientes com K-Means
- Recomendacoes personalizadas de vinhos
- Alertas estrategicos (estoque baixo, risco de churn)

## Tecnologias

- FastAPI
- Pandas, NumPy
- Scikit-learn

## Como Executar

```bash
poetry install
poetry run fastapi dev app/main.py
```

## Endpoints

- `GET /api/dashboard` - Resumo do dashboard
- `GET /api/clientes` - Lista de clientes
- `GET /api/clientes/{id}` - Detalhes do cliente
- `GET /api/produtos` - Lista de produtos
- `GET /api/alertas` - Alertas estrategicos
- `GET /api/churn` - Analise de churn
- `GET /api/segmentacao` - Segmentacao de clientes
- `GET /api/recomendacoes/{cliente_id}` - Recomendacoes
