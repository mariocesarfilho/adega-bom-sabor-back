# Adega Bom Sabor - Backend API

Sistema de Apoio a Decisao (SAD) para gestao de adega com recursos de Machine Learning.

## Funcionalidades

- **Previsao de Churn**: Modelo Random Forest para identificar clientes com risco de cancelamento
- **Segmentacao de Clientes**: Agrupamento K-Means em 3 segmentos (Premium, Sensivel a Promocoes, Ocasional)
- **Recomendacoes de Produtos**: Sugestoes personalizadas de vinhos baseadas no historico de compras
- **Alertas Estrategicos**: Notificacoes sobre estoque baixo e clientes em risco
- **Analytics**: Vendas por mes, top produtos, clientes por cidade

## Arquitetura

O projeto segue uma arquitetura em camadas seguindo principios SOLID:

```
app/
├── main.py              # Aplicacao FastAPI, CORS, routers
├── config.py            # Configuracoes (DATABASE_URL, etc)
├── database.py          # SQLAlchemy engine e sessao
├── models/              # Modelos SQLAlchemy (ORM)
│   ├── cliente.py
│   ├── produto.py
│   └── compra.py
├── schemas/             # Schemas Pydantic (validacao)
│   ├── cliente.py
│   ├── produto.py
│   ├── compra.py
│   └── dashboard.py
├── repositories/        # Camada de acesso a dados
│   ├── cliente_repository.py
│   ├── produto_repository.py
│   └── compra_repository.py
├── services/            # Logica de negocio e ML
│   ├── ml_service.py
│   ├── recommendation_service.py
│   ├── alert_service.py
│   └── analytics_service.py
└── routes/              # Endpoints da API
    ├── dashboard.py
    ├── clientes.py
    ├── produtos.py
    ├── compras.py
    └── analytics.py

scripts/
├── schema.sql           # DDL para criar tabelas
└── seed_data.sql        # Dados iniciais das planilhas
```

## Tecnologias

- **FastAPI** - Framework web async
- **SQLAlchemy 2.0** - ORM para PostgreSQL
- **PostgreSQL** - Banco de dados relacional
- **Pandas** - Manipulacao de dados
- **Scikit-learn** - Modelos de Machine Learning
- **Pydantic** - Validacao de dados

## Pre-requisitos

- Python 3.12+
- PostgreSQL 14+
- Poetry (gerenciador de dependencias)

## Instalacao

### 1. Clonar o repositorio

```bash
git clone https://github.com/mariocesarfilho/adega-bom-sabor-back.git
cd adega-bom-sabor-back
```

### 2. Instalar dependencias

```bash
poetry install
```

### 3. Configurar PostgreSQL

Criar o banco de dados:

```bash
# Conectar ao PostgreSQL
psql -U postgres

# Criar banco de dados
CREATE DATABASE adega_bom_sabor;

# Sair
\q
```

### 4. Criar tabelas

```bash
psql -U postgres -d adega_bom_sabor -f scripts/schema.sql
```

### 5. Inserir dados iniciais

```bash
psql -U postgres -d adega_bom_sabor -f scripts/seed_data.sql
```

### 6. Configurar variaveis de ambiente

Criar arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/adega_bom_sabor
DEBUG=false
```

Ajuste as credenciais conforme sua configuracao do PostgreSQL.

## Executar

### Modo desenvolvimento

```bash
poetry run fastapi dev app/main.py
```

O servidor estara disponivel em `http://localhost:8000`

### Modo producao

```bash
poetry run fastapi run app/main.py
```

## Endpoints da API

### Health Check
- `GET /healthz` - Verificar status da aplicacao

### Dashboard
- `GET /api/dashboard` - Resumo com KPIs e distribuicoes
- `GET /api/alertas` - Alertas estrategicos

### Clientes
- `GET /api/clientes` - Lista de clientes com churn e segmento
- `GET /api/clientes/{id}` - Detalhes do cliente com recomendacoes
- `GET /api/churn` - Analise de churn de todos os clientes
- `GET /api/segmentacao` - Segmentacao de todos os clientes
- `GET /api/recomendacoes/{id}` - Recomendacoes para um cliente

### Produtos
- `GET /api/produtos` - Lista de produtos

### Compras
- `GET /api/compras` - Lista de compras com detalhes

### Analytics
- `GET /api/analytics/vendas-por-mes` - Vendas agregadas por mes
- `GET /api/analytics/top-produtos` - Produtos mais vendidos
- `GET /api/analytics/clientes-por-cidade` - Clientes por cidade

### Machine Learning
- `POST /api/ml/retrain` - Retreinar modelos com dados atuais

## Documentacao da API

Apos iniciar o servidor, acesse:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Dependencias

```toml
[tool.poetry.dependencies]
python = "^3.12"
fastapi = {extras = ["standard"], version = "^0.122.0"}
sqlalchemy = "^2.0.0"
psycopg2-binary = "^2.9.9"
pandas = "^2.3.3"
scikit-learn = "^1.7.2"
numpy = "^2.3.5"
python-dotenv = "^1.0.0"
pydantic-settings = "^2.0.0"
```

## Notas sobre os Dados

- Os dados de clientes, produtos e compras foram extraidos das planilhas Excel fornecidas
- Os campos `estoque` e `preco` dos produtos sao valores sinteticos gerados para o prototipo
- Os modelos de ML sao treinados automaticamente na inicializacao da aplicacao
- Os labels de churn sao sinteticos, baseados em engajamento e recencia de compras

## Estrutura do Banco de Dados

### Tabela `clientes`
| Coluna | Tipo | Descricao |
|--------|------|-----------|
| cliente_id | INTEGER | Chave primaria |
| nome | VARCHAR(255) | Nome do cliente |
| idade | INTEGER | Idade |
| cidade | VARCHAR(100) | Cidade |
| pontuacao_engajamento | DECIMAL(4,2) | Pontuacao de 1 a 10 |
| assinante_clube | BOOLEAN | Assinante do clube |

### Tabela `produtos`
| Coluna | Tipo | Descricao |
|--------|------|-----------|
| produto_id | INTEGER | Chave primaria |
| nome | VARCHAR(255) | Nome do vinho |
| pais | VARCHAR(100) | Pais de origem |
| safra | INTEGER | Ano da safra |
| tipo_uva | VARCHAR(100) | Tipo de uva |
| estoque | INTEGER | Quantidade em estoque |
| preco | DECIMAL(10,2) | Preco unitario |

### Tabela `compras`
| Coluna | Tipo | Descricao |
|--------|------|-----------|
| compra_id | INTEGER | Chave primaria |
| cliente_id | INTEGER | FK para clientes |
| produto_id | INTEGER | FK para produtos |
| valor | DECIMAL(10,2) | Valor da compra |
| quantidade | INTEGER | Quantidade |
| data_compra | DATE | Data da compra |

## Licenca

Este projeto foi desenvolvido como prototipo para a Adega Bom Sabor.
