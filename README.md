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



Aqui está um modelo de **README.md** que você pode usar para o seu projeto. Basta colar no seu arquivo `README.md`:

````markdown
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
````

### 2. Criar um Ambiente Virtual

Navegue até a pasta do projeto e crie um ambiente virtual:

```bash
cd adega-bom-sabor-back
python -m venv venv
```

### 3. Ativar o Ambiente Virtual

Ative o ambiente virtual:

```bash
.\venv\Scripts\activate
```

### 4. Instalar as Dependências

Com o ambiente virtual ativo, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Se o arquivo `requirements.txt` não estiver presente, instale as dependências manualmente:

```bash
pip install fastapi uvicorn pandas scikit-learn psycopg openpyxl
```

### 5. Rodar a Aplicação

Para rodar o servidor de desenvolvimento, execute o comando abaixo:

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

A aplicação estará disponível em `http://localhost:8000`.

### 6. Acessar a Documentação

A documentação interativa da API estará disponível em:

```
http://localhost:8000/docs
```

### 7. Outras Dependências

Se você não tiver o **Poetry** instalado, instale com:

```bash
pip install poetry
```

E depois use o comando:

```bash
poetry install
```

Isso instalará todas as dependências definidas no `pyproject.toml`.

## Tecnologias Utilizadas

* **FastAPI**: Framework para construir APIs modernas e rápidas.
* **Uvicorn**: Servidor ASGI rápido.
* **Pandas**: Manipulação e análise de dados.
* **Scikit-learn**: Ferramentas de aprendizado de máquina.
* **PostgreSQL**: Banco de dados para armazenar dados relacionados à adega.

## Contribuições

Se você deseja contribuir para o projeto, por favor, faça um fork do repositório, crie uma branch para a sua alteração e envie um pull request com a sua contribuição.

---

**Autor:** Seu Nome
**Data de Criação:** 2025

```

### Explicação

- **Dependências**: Lista as bibliotecas que o projeto usa.
- **Instalação**: Instruções sobre como configurar o ambiente local no Windows, incluindo a criação de um ambiente virtual e a instalação das dependências.
- **Rodar a Aplicação**: Comandos para rodar o servidor local e acessar a documentação interativa da API.
- **Tecnologias Utilizadas**: Menciona as ferramentas e bibliotecas principais usadas no projeto.

Você pode ajustar o nome do repositório, autor e qualquer outra informação conforme necessário. Isso deve te ajudar a ter um README claro e completo para seu projeto! Se precisar de mais alguma coisa, só avisar.
```
