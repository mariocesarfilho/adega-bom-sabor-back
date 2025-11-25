# Adega Bom Sabor - Backend API

Sistema de Apoio a Decisao (SAD) para gestao de adega com recursos de Machine Learning e IA Simbolica.

## Funcionalidades

### Machine Learning
- **Previsao de Churn**: Modelo Random Forest usando dados REAIS de cancelamento (campo `cancelou_assinatura`)
- **Segmentacao de Clientes**: Agrupamento K-Means em 3 segmentos (Premium, Sensivel a Promocoes, Ocasional)
- **Recomendacoes de Produtos**: Filtragem baseada em conteudo usando atributos do produto (tipo_uva, pais, safra)

### IA Simbolica (Regras SE-ENTAO)
- **Cliente Inativo**: SE cliente > 60 dias sem comprar → marcar como inativo e sugerir reativacao
- **Fidelidade de Uva**: SE comprou 3 meses seguidos o mesmo tipo de uva → recomendar semelhantes
- **Demanda Crescente**: SE demanda historica aumenta → alerta estrategico de reposicao (conceitual)

### Analytics
- Vendas por mes, top produtos, clientes por cidade
- Dashboard com KPIs e distribuicoes

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
- Poetry (recomendado) ou pip

## Instalacao

### Windows

#### 1. Instalar Python 3.12+
Baixe e instale do site oficial: https://www.python.org/downloads/

Certifique-se de marcar "Add Python to PATH" durante a instalacao.

#### 2. Instalar PostgreSQL
Baixe e instale do site oficial: https://www.postgresql.org/download/windows/

Durante a instalacao, anote a senha do usuario `postgres`.

#### 3. Clonar o repositorio
```cmd
git clone https://github.com/mariocesarfilho/adega-bom-sabor-back.git
cd adega-bom-sabor-back
```

#### 4. Criar ambiente virtual e instalar dependencias

**Opcao A: Usando Poetry (recomendado)**
```cmd
pip install poetry
poetry install
```

**Opcao B: Usando pip**
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### 5. Configurar PostgreSQL
Abra o SQL Shell (psql) ou pgAdmin e execute:
```sql
CREATE DATABASE adega_bom_sabor;
```

#### 6. Criar tabelas e inserir dados
```cmd
psql -U postgres -d adega_bom_sabor -f scripts\schema.sql
psql -U postgres -d adega_bom_sabor -f scripts\seed_data.sql
```

#### 7. Configurar variaveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
DATABASE_URL=postgresql://postgres:SUA_SENHA@localhost:5432/adega_bom_sabor
DEBUG=false
```

#### 8. Executar o servidor
**Com Poetry:**
```cmd
poetry run fastapi dev app/main.py
```

**Com pip:**
```cmd
venv\Scripts\activate
fastapi dev app/main.py
```

### Linux / Mac

#### 1. Instalar Python 3.12+
**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3.12 python3.12-venv python3-pip
```

**Mac (usando Homebrew):**
```bash
brew install python@3.12
```

#### 2. Instalar PostgreSQL
**Ubuntu/Debian:**
```bash
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

**Mac (usando Homebrew):**
```bash
brew install postgresql@14
brew services start postgresql@14
```

#### 3. Clonar o repositorio
```bash
git clone https://github.com/mariocesarfilho/adega-bom-sabor-back.git
cd adega-bom-sabor-back
```

#### 4. Criar ambiente virtual e instalar dependencias

**Opcao A: Usando Poetry (recomendado)**
```bash
pip install poetry
poetry install
```

**Opcao B: Usando pip**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 5. Configurar PostgreSQL
```bash
# Conectar ao PostgreSQL
sudo -u postgres psql

# Criar banco de dados
CREATE DATABASE adega_bom_sabor;

# Criar usuario (opcional)
CREATE USER adega_user WITH PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE adega_bom_sabor TO adega_user;

# Sair
\q
```

#### 6. Criar tabelas e inserir dados
```bash
sudo -u postgres psql -d adega_bom_sabor -f scripts/schema.sql
sudo -u postgres psql -d adega_bom_sabor -f scripts/seed_data.sql
```

#### 7. Configurar variaveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/adega_bom_sabor
DEBUG=false
```

#### 8. Executar o servidor
**Com Poetry:**
```bash
poetry run fastapi dev app/main.py
```

**Com pip:**
```bash
source venv/bin/activate
fastapi dev app/main.py
```

## Acessar a Aplicacao

Apos iniciar o servidor, acesse:
- API: http://localhost:8000
- Documentacao Swagger: http://localhost:8000/docs
- Documentacao ReDoc: http://localhost:8000/redoc

## Modo Producao

Para executar em modo producao:

**Com Poetry:**
```bash
poetry run fastapi run app/main.py
```

**Com pip:**
```bash
fastapi run app/main.py
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

## Notas IMPORTANTES sobre os Dados

### Dados Reais das Planilhas Excel
- Todos os dados de clientes, produtos e compras foram extraidos das planilhas Excel fornecidas
- **A base real NAO possui preco nem estoque em produtos**
- O preco esta na tabela de compras (campo `valor` da transacao)
- Os modelos de ML sao treinados automaticamente na inicializacao da aplicacao
- **Os labels de churn sao REAIS** (campo `cancelou_assinatura` da planilha Cliente.xlsx)

### Regras de Estoque (Conceituais)
As regras de estoque mencionadas no sistema sao apenas **conceituais/simbolicas** para fins academicos:
- Nao ha campo de estoque no banco de dados
- Nao ha geracao de valores sinteticos de estoque
- Alertas de "demanda crescente" sao baseados em tendencias de compras, nao em niveis de estoque

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
| **cancelou_assinatura** | **BOOLEAN** | **Label real de churn** |

### Tabela `produtos`
| Coluna | Tipo | Descricao |
|--------|------|-----------|
| produto_id | INTEGER | Chave primaria |
| nome | VARCHAR(255) | Nome do vinho |
| pais | VARCHAR(100) | Pais de origem |
| safra | INTEGER | Ano da safra |
| tipo_uva | VARCHAR(100) | Tipo de uva |

**IMPORTANTE**: Esta tabela NAO possui campos `estoque` nem `preco` conforme a base real.

### Tabela `compras`
| Coluna | Tipo | Descricao |
|--------|------|-----------|
| compra_id | INTEGER | Chave primaria |
| cliente_id | INTEGER | FK para clientes |
| produto_id | INTEGER | FK para produtos |
| **valor** | **DECIMAL(10,2)** | **Preco real da transacao** |
| quantidade | INTEGER | Quantidade |
| data_compra | DATE | Data da compra |

## ETL e Feature Engineering

O sistema realiza ETL automatico na inicializacao:

### Features Calculadas
- `frequencia_compra`: Total de compras do cliente
- `dias_desde_ultima_compra`: Recencia da ultima compra
- `ticket_medio`: SUM(valor) / COUNT(compras)
- `tipo_preferido`: Tipo de uva mais comprado
- `pais_preferido`: Pais mais comprado

### Modelos de ML

#### 1. Predicao de Churn (RandomForest)
- **Label**: `cancelou_assinatura` (dados reais da planilha)
- **Features**: frequencia_compra, ticket_medio, dias_desde_ultima_compra, pontuacao_engajamento, assinante_clube
- **Saida**: probabilidade_de_churn (0 a 1)

#### 2. Segmentacao (KMeans)
- **Features**: ticket_medio, quantidade de compras, recorrencia, engajamento
- **Clusters**: Premium, Sensivel a Promocoes, Ocasional

#### 3. Recomendacao (Filtragem Baseada em Conteudo)
- **Atributos**: tipo_uva, safra, pais
- **Metodo**: Similaridade baseada em historico de compras

## Licenca

Este projeto foi desenvolvido como prototipo para a Adega Bom Sabor.
