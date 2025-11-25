-- Schema SQL para Adega Bom Sabor - Sistema de Apoio a Decisao
-- Execute este script para criar as tabelas no PostgreSQL

-- Criar banco de dados (execute separadamente se necessario)
-- CREATE DATABASE adega_bom_sabor;

-- Conectar ao banco de dados
-- \c adega_bom_sabor

-- Remover tabelas existentes (cuidado em producao!)
DROP TABLE IF EXISTS compras CASCADE;
DROP TABLE IF EXISTS produtos CASCADE;
DROP TABLE IF EXISTS clientes CASCADE;

-- Tabela de Clientes
CREATE TABLE clientes (
    cliente_id INTEGER PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    idade INTEGER NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    pontuacao_engajamento DECIMAL(4,2) NOT NULL,
    assinante_clube BOOLEAN DEFAULT FALSE
);

-- Indices para clientes
CREATE INDEX idx_clientes_cidade ON clientes(cidade);
CREATE INDEX idx_clientes_assinante ON clientes(assinante_clube);

-- Tabela de Produtos (Vinhos)
CREATE TABLE produtos (
    produto_id INTEGER PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    safra INTEGER NOT NULL,
    tipo_uva VARCHAR(100) NOT NULL,
    estoque INTEGER NOT NULL DEFAULT 50,
    preco DECIMAL(10,2) NOT NULL DEFAULT 100.00
);

-- Indices para produtos
CREATE INDEX idx_produtos_pais ON produtos(pais);
CREATE INDEX idx_produtos_tipo_uva ON produtos(tipo_uva);
CREATE INDEX idx_produtos_estoque ON produtos(estoque);

-- Tabela de Compras
CREATE TABLE compras (
    compra_id INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL REFERENCES clientes(cliente_id),
    produto_id INTEGER NOT NULL REFERENCES produtos(produto_id),
    valor DECIMAL(10,2) NOT NULL,
    quantidade INTEGER NOT NULL,
    data_compra DATE NOT NULL
);

-- Indices para compras
CREATE INDEX idx_compras_cliente ON compras(cliente_id);
CREATE INDEX idx_compras_produto ON compras(produto_id);
CREATE INDEX idx_compras_data ON compras(data_compra);

-- Comentarios nas tabelas
COMMENT ON TABLE clientes IS 'Tabela de clientes da adega';
COMMENT ON TABLE produtos IS 'Tabela de produtos (vinhos) da adega';
COMMENT ON TABLE compras IS 'Tabela de compras realizadas pelos clientes';

COMMENT ON COLUMN clientes.pontuacao_engajamento IS 'Pontuacao de engajamento do cliente (1-10)';
COMMENT ON COLUMN clientes.assinante_clube IS 'Indica se o cliente e assinante do clube de vinhos';
COMMENT ON COLUMN produtos.estoque IS 'Quantidade em estoque (valor sintetico para prototipo)';
COMMENT ON COLUMN produtos.preco IS 'Preco do produto (valor sintetico para prototipo)';
