from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime, timedelta
import random

app = FastAPI(title="Adega Bom Sabor - SAD")

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# In-memory database
clientes_db = []
produtos_db = []
compras_db = []
alertas_db = []

# ML Models
churn_model = None
segmentation_model = None
scaler = None

def clean_excel_data(df):
    """Clean Excel data that has merged rows with newlines"""
    cleaned_rows = []
    for _, row in df.iterrows():
        row_values = [str(v) for v in row.values]
        if any('\n' in v for v in row_values):
            splits = [v.split('\n') for v in row_values]
            max_splits = max(len(s) for s in splits)
            for i in range(max_splits):
                new_row = []
                for s in splits:
                    if i < len(s):
                        new_row.append(s[i].strip())
                    else:
                        new_row.append(s[-1].strip())
                cleaned_rows.append(new_row)
        else:
            cleaned_rows.append(row_values)
    return pd.DataFrame(cleaned_rows, columns=df.columns)

def load_initial_data():
    """Load data from Excel files"""
    global clientes_db, produtos_db, compras_db
    
    try:
        # Load clientes
        clientes_df = pd.read_excel('/home/ubuntu/attachments/eba9e8a4-19c6-4339-ad53-9fa7e150417d/clientes.xlsx')
        clientes_df = clean_excel_data(clientes_df)
        clientes_df['cliente_id'] = pd.to_numeric(clientes_df['cliente_id'])
        clientes_df['idade'] = pd.to_numeric(clientes_df['idade'])
        clientes_df['pontuacao_enga'] = pd.to_numeric(clientes_df['pontuacao_enga'])
        
        for _, row in clientes_df.iterrows():
            clientes_db.append({
                "cliente_id": int(row['cliente_id']),
                "nome": row['nome'],
                "idade": int(row['idade']),
                "cidade": row['cidade'],
                "pontuacao_engajamento": float(row['pontuacao_enga']),
                "assinante_clube": row['assinante_clube'] == 'Sim'
            })
        
        # Load produtos
        produtos_df = pd.read_excel('/home/ubuntu/attachments/51cdf739-d671-462a-9206-796d574c602f/produtos.xlsx')
        produtos_df = clean_excel_data(produtos_df)
        produtos_df['produto_id'] = pd.to_numeric(produtos_df['produto_id'])
        produtos_df['safra'] = pd.to_numeric(produtos_df['safra'])
        
        for _, row in produtos_df.iterrows():
            produtos_db.append({
                "produto_id": int(row['produto_id']),
                "nome": row['nome'],
                "pais": row['pais'],
                "safra": int(row['safra']),
                "tipo_uva": row['tipo_uva'],
                "estoque": random.randint(5, 100),
                "preco": round(random.uniform(50, 500), 2)
            })
        
        # Load compras
        compras_df = pd.read_excel('/home/ubuntu/attachments/9aeecfd3-c8ba-448f-a547-5a4f661b5ec4/compras.xlsx')
        compras_df.columns = compras_df.iloc[0].values
        compras_df = compras_df.iloc[1:].reset_index(drop=True)
        compras_df = clean_excel_data(compras_df)
        compras_df['compra_id'] = pd.to_numeric(compras_df['compra_id'])
        compras_df['cliente_id'] = pd.to_numeric(compras_df['cliente_id'])
        compras_df['produto_id'] = pd.to_numeric(compras_df['produto_id'])
        compras_df['valor'] = pd.to_numeric(compras_df['valor'])
        compras_df['quantidade'] = pd.to_numeric(compras_df['quantidade'])
        
        for _, row in compras_df.iterrows():
            compras_db.append({
                "compra_id": int(row['compra_id']),
                "cliente_id": int(row['cliente_id']),
                "produto_id": int(row['produto_id']),
                "valor": float(row['valor']),
                "quantidade": int(row['quantidade']),
                "data_compra": str(row['data_compra'])[:10]
            })
        
        print(f"Loaded {len(clientes_db)} clientes, {len(produtos_db)} produtos, {len(compras_db)} compras")
        
    except Exception as e:
        print(f"Error loading data: {e}")
        # Create sample data if files not found
        create_sample_data()

def create_sample_data():
    """Create sample data if Excel files are not available"""
    global clientes_db, produtos_db, compras_db
    
    cidades = ["Sao Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre", "Salvador", "Brasilia", "Fortaleza"]
    
    for i in range(1, 51):
        clientes_db.append({
            "cliente_id": i,
            "nome": f"Cliente {i}",
            "idade": random.randint(25, 70),
            "cidade": random.choice(cidades),
            "pontuacao_engajamento": round(random.uniform(1, 10), 2),
            "assinante_clube": random.choice([True, False])
        })
    
    tipos_uva = ["Merlot", "Cabernet Sauvignon", "Chardonnay", "Pinot Noir", "Malbec", "Syrah", "Sauvignon Blanc", "Tempranillo"]
    paises = ["Franca", "Italia", "Chile", "Argentina", "Brasil", "Portugal", "Espanha", "Africa do Sul"]
    
    for i in range(1, 101):
        produtos_db.append({
            "produto_id": i,
            "nome": f"Vinho {i}",
            "pais": random.choice(paises),
            "safra": random.randint(2015, 2023),
            "tipo_uva": random.choice(tipos_uva),
            "estoque": random.randint(5, 100),
            "preco": round(random.uniform(50, 500), 2)
        })
    
    for i in range(1, 201):
        compras_db.append({
            "compra_id": i,
            "cliente_id": random.randint(1, 50),
            "produto_id": random.randint(1, 100),
            "valor": round(random.uniform(50, 500), 2),
            "quantidade": random.randint(1, 6),
            "data_compra": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d")
        })

def train_models():
    """Train ML models for churn prediction and customer segmentation"""
    global churn_model, segmentation_model, scaler
    
    if len(clientes_db) == 0 or len(compras_db) == 0:
        return
    
    # Prepare customer features
    customer_features = []
    for cliente in clientes_db:
        cliente_compras = [c for c in compras_db if c['cliente_id'] == cliente['cliente_id']]
        
        total_compras = len(cliente_compras)
        valor_total = sum(c['valor'] for c in cliente_compras)
        valor_medio = valor_total / total_compras if total_compras > 0 else 0
        qtd_total = sum(c['quantidade'] for c in cliente_compras)
        
        # Calculate recency (days since last purchase)
        if cliente_compras:
            datas = []
            for c in cliente_compras:
                try:
                    datas.append(datetime.strptime(c['data_compra'][:10], "%Y-%m-%d"))
                except:
                    pass
            if datas:
                ultima_compra = max(datas)
                recencia = (datetime.now() - ultima_compra).days
            else:
                recencia = 365
        else:
            recencia = 365
        
        customer_features.append({
            'cliente_id': cliente['cliente_id'],
            'idade': cliente['idade'],
            'pontuacao_engajamento': cliente['pontuacao_engajamento'],
            'assinante': 1 if cliente['assinante_clube'] else 0,
            'total_compras': total_compras,
            'valor_total': valor_total,
            'valor_medio': valor_medio,
            'qtd_total': qtd_total,
            'recencia': recencia
        })
    
    df_features = pd.DataFrame(customer_features)
    
    # Features for clustering
    feature_cols = ['idade', 'pontuacao_engajamento', 'total_compras', 'valor_total', 'valor_medio', 'recencia']
    X = df_features[feature_cols].values
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Train segmentation model (KMeans with 3 clusters)
    segmentation_model = KMeans(n_clusters=3, random_state=42, n_init=10)
    segmentation_model.fit(X_scaled)
    
    # Train churn prediction model
    # Create synthetic churn labels based on engagement and recency
    y_churn = []
    for _, row in df_features.iterrows():
        # Higher probability of churn if low engagement and high recency
        churn_prob = (10 - row['pontuacao_engajamento']) / 10 * 0.5 + (row['recencia'] / 365) * 0.5
        y_churn.append(1 if churn_prob > 0.5 else 0)
    
    churn_model = RandomForestClassifier(n_estimators=50, random_state=42)
    churn_model.fit(X_scaled, y_churn)
    
    print("Models trained successfully")

def generate_alerts():
    """Generate strategic alerts"""
    global alertas_db
    alertas_db = []
    
    # Alert for low stock products
    for produto in produtos_db:
        if produto['estoque'] < 20:
            alertas_db.append({
                "tipo": "estoque_baixo",
                "severidade": "alta" if produto['estoque'] < 10 else "media",
                "mensagem": f"Produto '{produto['nome']}' com estoque baixo: {produto['estoque']} unidades",
                "produto_id": produto['produto_id']
            })
    
    # Alert for high churn risk customers
    for cliente in clientes_db:
        churn_prob = calculate_churn_probability(cliente['cliente_id'])
        if churn_prob > 0.7:
            alertas_db.append({
                "tipo": "risco_churn",
                "severidade": "alta",
                "mensagem": f"Cliente '{cliente['nome']}' com alta probabilidade de cancelamento: {churn_prob*100:.1f}%",
                "cliente_id": cliente['cliente_id']
            })
        elif churn_prob > 0.5:
            alertas_db.append({
                "tipo": "risco_churn",
                "severidade": "media",
                "mensagem": f"Cliente '{cliente['nome']}' com probabilidade moderada de cancelamento: {churn_prob*100:.1f}%",
                "cliente_id": cliente['cliente_id']
            })

def calculate_churn_probability(cliente_id: int) -> float:
    """Calculate churn probability for a customer"""
    global churn_model, scaler
    
    cliente = next((c for c in clientes_db if c['cliente_id'] == cliente_id), None)
    if not cliente or churn_model is None:
        return 0.5
    
    cliente_compras = [c for c in compras_db if c['cliente_id'] == cliente_id]
    
    total_compras = len(cliente_compras)
    valor_total = sum(c['valor'] for c in cliente_compras)
    valor_medio = valor_total / total_compras if total_compras > 0 else 0
    
    if cliente_compras:
        datas = []
        for c in cliente_compras:
            try:
                datas.append(datetime.strptime(c['data_compra'][:10], "%Y-%m-%d"))
            except:
                pass
        if datas:
            ultima_compra = max(datas)
            recencia = (datetime.now() - ultima_compra).days
        else:
            recencia = 365
    else:
        recencia = 365
    
    features = np.array([[
        cliente['idade'],
        cliente['pontuacao_engajamento'],
        total_compras,
        valor_total,
        valor_medio,
        recencia
    ]])
    
    features_scaled = scaler.transform(features)
    proba = churn_model.predict_proba(features_scaled)[0]
    
    # Handle case where model only has one class
    if len(proba) == 1:
        # Use heuristic based on engagement and recency
        churn_score = (10 - cliente['pontuacao_engajamento']) / 10 * 0.5 + (recencia / 365) * 0.5
        return float(min(max(churn_score, 0), 1))
    
    return float(proba[1])

def get_customer_segment(cliente_id: int) -> dict:
    """Get customer segment"""
    global segmentation_model, scaler
    
    cliente = next((c for c in clientes_db if c['cliente_id'] == cliente_id), None)
    if not cliente or segmentation_model is None:
        return {"segmento": "Desconhecido", "descricao": "Dados insuficientes"}
    
    cliente_compras = [c for c in compras_db if c['cliente_id'] == cliente_id]
    
    total_compras = len(cliente_compras)
    valor_total = sum(c['valor'] for c in cliente_compras)
    valor_medio = valor_total / total_compras if total_compras > 0 else 0
    
    if cliente_compras:
        datas = []
        for c in cliente_compras:
            try:
                datas.append(datetime.strptime(c['data_compra'][:10], "%Y-%m-%d"))
            except:
                pass
        if datas:
            ultima_compra = max(datas)
            recencia = (datetime.now() - ultima_compra).days
        else:
            recencia = 365
    else:
        recencia = 365
    
    features = np.array([[
        cliente['idade'],
        cliente['pontuacao_engajamento'],
        total_compras,
        valor_total,
        valor_medio,
        recencia
    ]])
    
    features_scaled = scaler.transform(features)
    cluster = segmentation_model.predict(features_scaled)[0]
    
    segment_names = {
        0: {"segmento": "Premium", "descricao": "Clientes de alto valor com compras frequentes e alto engajamento"},
        1: {"segmento": "Sensivel a Promocoes", "descricao": "Clientes que respondem bem a ofertas e descontos"},
        2: {"segmento": "Ocasional", "descricao": "Clientes com compras esporadicas, potencial de crescimento"}
    }
    
    return segment_names.get(cluster, {"segmento": "Desconhecido", "descricao": "Segmento nao identificado"})

def get_product_recommendations(cliente_id: int, limit: int = 5) -> list:
    """Get product recommendations for a customer"""
    cliente = next((c for c in clientes_db if c['cliente_id'] == cliente_id), None)
    if not cliente:
        return []
    
    # Get customer's purchase history
    cliente_compras = [c for c in compras_db if c['cliente_id'] == cliente_id]
    produtos_comprados = set(c['produto_id'] for c in cliente_compras)
    
    # Get preferred grape types and countries
    tipos_uva_preferidos = {}
    paises_preferidos = {}
    
    for compra in cliente_compras:
        produto = next((p for p in produtos_db if p['produto_id'] == compra['produto_id']), None)
        if produto:
            tipos_uva_preferidos[produto['tipo_uva']] = tipos_uva_preferidos.get(produto['tipo_uva'], 0) + 1
            paises_preferidos[produto['pais']] = paises_preferidos.get(produto['pais'], 0) + 1
    
    # Score products
    scored_products = []
    for produto in produtos_db:
        if produto['produto_id'] in produtos_comprados:
            continue
        
        score = 0
        # Bonus for preferred grape type
        if produto['tipo_uva'] in tipos_uva_preferidos:
            score += tipos_uva_preferidos[produto['tipo_uva']] * 2
        # Bonus for preferred country
        if produto['pais'] in paises_preferidos:
            score += paises_preferidos[produto['pais']] * 1.5
        # Bonus for recent vintages
        if produto['safra'] >= 2020:
            score += 1
        # Random factor for diversity
        score += random.uniform(0, 1)
        
        scored_products.append({
            **produto,
            "score": score,
            "motivo": f"Baseado em suas preferencias por {produto['tipo_uva']} e vinhos de {produto['pais']}"
        })
    
    # Sort by score and return top recommendations
    scored_products.sort(key=lambda x: x['score'], reverse=True)
    return scored_products[:limit]

# Startup event
@app.on_event("startup")
async def startup_event():
    load_initial_data()
    train_models()
    generate_alerts()

# API Endpoints
@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/api/dashboard")
async def get_dashboard():
    """Get dashboard summary data"""
    total_clientes = len(clientes_db)
    total_produtos = len(produtos_db)
    total_compras = len(compras_db)
    valor_total_vendas = sum(c['valor'] * c['quantidade'] for c in compras_db)
    
    # Churn distribution
    churn_alto = 0
    churn_medio = 0
    churn_baixo = 0
    
    for cliente in clientes_db:
        prob = calculate_churn_probability(cliente['cliente_id'])
        if prob > 0.7:
            churn_alto += 1
        elif prob > 0.4:
            churn_medio += 1
        else:
            churn_baixo += 1
    
    # Segment distribution
    segmentos = {"Premium": 0, "Sensivel a Promocoes": 0, "Ocasional": 0}
    for cliente in clientes_db:
        seg = get_customer_segment(cliente['cliente_id'])
        if seg['segmento'] in segmentos:
            segmentos[seg['segmento']] += 1
    
    return {
        "total_clientes": total_clientes,
        "total_produtos": total_produtos,
        "total_compras": total_compras,
        "valor_total_vendas": round(valor_total_vendas, 2),
        "churn_distribution": {
            "alto": churn_alto,
            "medio": churn_medio,
            "baixo": churn_baixo
        },
        "segment_distribution": segmentos,
        "alertas_count": len(alertas_db)
    }

@app.get("/api/clientes")
async def get_clientes():
    """Get all customers with churn probability and segment"""
    result = []
    for cliente in clientes_db:
        churn_prob = calculate_churn_probability(cliente['cliente_id'])
        segment = get_customer_segment(cliente['cliente_id'])
        
        cliente_compras = [c for c in compras_db if c['cliente_id'] == cliente['cliente_id']]
        total_gasto = sum(c['valor'] * c['quantidade'] for c in cliente_compras)
        
        result.append({
            **cliente,
            "churn_probability": round(churn_prob, 2),
            "segmento": segment['segmento'],
            "segmento_descricao": segment['descricao'],
            "total_compras": len(cliente_compras),
            "total_gasto": round(total_gasto, 2)
        })
    
    return result

@app.get("/api/clientes/{cliente_id}")
async def get_cliente(cliente_id: int):
    """Get customer details with recommendations"""
    cliente = next((c for c in clientes_db if c['cliente_id'] == cliente_id), None)
    if not cliente:
        return {"error": "Cliente nao encontrado"}
    
    churn_prob = calculate_churn_probability(cliente_id)
    segment = get_customer_segment(cliente_id)
    recommendations = get_product_recommendations(cliente_id)
    
    cliente_compras = [c for c in compras_db if c['cliente_id'] == cliente_id]
    historico = []
    for compra in cliente_compras:
        produto = next((p for p in produtos_db if p['produto_id'] == compra['produto_id']), None)
        historico.append({
            **compra,
            "produto_nome": produto['nome'] if produto else "Desconhecido"
        })
    
    return {
        **cliente,
        "churn_probability": round(churn_prob, 2),
        "segmento": segment['segmento'],
        "segmento_descricao": segment['descricao'],
        "recomendacoes": recommendations,
        "historico_compras": historico
    }

@app.get("/api/produtos")
async def get_produtos():
    """Get all products"""
    return produtos_db

@app.get("/api/compras")
async def get_compras():
    """Get all purchases"""
    result = []
    for compra in compras_db:
        cliente = next((c for c in clientes_db if c['cliente_id'] == compra['cliente_id']), None)
        produto = next((p for p in produtos_db if p['produto_id'] == compra['produto_id']), None)
        result.append({
            **compra,
            "cliente_nome": cliente['nome'] if cliente else "Desconhecido",
            "produto_nome": produto['nome'] if produto else "Desconhecido"
        })
    return result

@app.get("/api/alertas")
async def get_alertas():
    """Get strategic alerts"""
    return alertas_db

@app.get("/api/churn")
async def get_churn_analysis():
    """Get churn analysis for all customers"""
    result = []
    for cliente in clientes_db:
        prob = calculate_churn_probability(cliente['cliente_id'])
        result.append({
            "cliente_id": cliente['cliente_id'],
            "nome": cliente['nome'],
            "churn_probability": round(prob, 2),
            "risco": "Alto" if prob > 0.7 else ("Medio" if prob > 0.4 else "Baixo")
        })
    
    result.sort(key=lambda x: x['churn_probability'], reverse=True)
    return result

@app.get("/api/segmentacao")
async def get_segmentacao():
    """Get customer segmentation"""
    result = []
    for cliente in clientes_db:
        segment = get_customer_segment(cliente['cliente_id'])
        cliente_compras = [c for c in compras_db if c['cliente_id'] == cliente['cliente_id']]
        total_gasto = sum(c['valor'] * c['quantidade'] for c in cliente_compras)
        
        result.append({
            "cliente_id": cliente['cliente_id'],
            "nome": cliente['nome'],
            "segmento": segment['segmento'],
            "descricao": segment['descricao'],
            "total_compras": len(cliente_compras),
            "total_gasto": round(total_gasto, 2)
        })
    
    return result

@app.get("/api/recomendacoes/{cliente_id}")
async def get_recomendacoes(cliente_id: int, limit: int = 5):
    """Get product recommendations for a customer"""
    recommendations = get_product_recommendations(cliente_id, limit)
    return recommendations

@app.get("/api/analytics/vendas-por-mes")
async def get_vendas_por_mes():
    """Get sales by month"""
    vendas_mes = {}
    for compra in compras_db:
        try:
            data = compra['data_compra'][:7]  # YYYY-MM
            if data not in vendas_mes:
                vendas_mes[data] = {"mes": data, "valor": 0, "quantidade": 0}
            vendas_mes[data]['valor'] += compra['valor'] * compra['quantidade']
            vendas_mes[data]['quantidade'] += compra['quantidade']
        except:
            pass
    
    result = list(vendas_mes.values())
    result.sort(key=lambda x: x['mes'])
    return result

@app.get("/api/analytics/top-produtos")
async def get_top_produtos():
    """Get top selling products"""
    produto_vendas = {}
    for compra in compras_db:
        pid = compra['produto_id']
        if pid not in produto_vendas:
            produto = next((p for p in produtos_db if p['produto_id'] == pid), None)
            produto_vendas[pid] = {
                "produto_id": pid,
                "nome": produto['nome'] if produto else f"Produto {pid}",
                "quantidade_vendida": 0,
                "valor_total": 0
            }
        produto_vendas[pid]['quantidade_vendida'] += compra['quantidade']
        produto_vendas[pid]['valor_total'] += compra['valor'] * compra['quantidade']
    
    result = list(produto_vendas.values())
    result.sort(key=lambda x: x['valor_total'], reverse=True)
    return result[:10]

@app.get("/api/analytics/clientes-por-cidade")
async def get_clientes_por_cidade():
    """Get customers by city"""
    cidades = {}
    for cliente in clientes_db:
        cidade = cliente['cidade']
        if cidade not in cidades:
            cidades[cidade] = {"cidade": cidade, "quantidade": 0}
        cidades[cidade]['quantidade'] += 1
    
    return list(cidades.values())
