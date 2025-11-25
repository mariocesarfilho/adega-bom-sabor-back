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

criar ambiente virutal

python -m venv venv

- windows
venv\Scripts\activate

# No Linux/Mac
source venv/bin/activate




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



# Projeto Adega Bom Sabor - Backend

Este é o backend do projeto **Adega Bom Sabor**, desenvolvido utilizando **FastAPI**, com várias bibliotecas e funcionalidades para manipulação de dados e análise de informações.

## Dependências

Este projeto utiliza as seguintes dependências:

- **FastAPI**: Framework para construção de APIs rápidas.
- **Uvicorn**: Servidor ASGI para executar a aplicação FastAPI.
- **Pandas**: Para análise e manipulação de dados.
- **scikit-learn**: Para tarefas de aprendizado de máquina, incluindo clustering.
- **psycopg**: Biblioteca para conectar-se ao banco de dados PostgreSQL.
- **openpyxl**: Para manipulação de arquivos Excel (.xlsx).

## Como Instalar e Rodar no Windows

### 1. Clonar o Repositório

Primeiro, clone o repositório do projeto para a sua máquina local:

```bash
git clone https://github.com/seu_usuario/adega-bom-sabor-back.git
