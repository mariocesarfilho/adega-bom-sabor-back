-- Seed data SQL para Adega Bom Sabor - Sistema de Apoio a Decisao
-- Dados REAIS extraidos das planilhas Excel fornecidas
-- Execute este script apos o schema.sql para inserir os dados iniciais

-- =====================
-- CLIENTES
-- Dados reais da planilha Cliente.xlsx
-- =====================

INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (1, 'Cliente 1', 66, 'Fortaleza', 4.45, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (2, 'Cliente 2', 32, 'Salvador', 9.57, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (3, 'Cliente 3', 41, 'Belo Horizonte', 6.31, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (4, 'Cliente 4', 29, 'Curitiba', 7.82, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (5, 'Cliente 5', 60, 'Brasília', 3.29, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (6, 'Cliente 6', 33, 'Goiânia', 5.00, FALSE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (7, 'Cliente 7', 68, 'Rio de Janeiro', 5.91, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (8, 'Cliente 8', 54, 'Brasília', 9.88, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (9, 'Cliente 9', 47, 'Fortaleza', 8.14, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (10, 'Cliente 10', 65, 'Belo Horizonte', 3.27, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (11, 'Cliente 11', 51, 'Rio de Janeiro', 1.63, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (12, 'Cliente 12', 39, 'Curitiba', 5.27, FALSE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (13, 'Cliente 13', 37, 'São Paulo', 2.55, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (14, 'Cliente 14', 42, 'Curitiba', 6.47, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (15, 'Cliente 15', 34, 'Salvador', 5.00, FALSE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (16, 'Cliente 16', 62, 'Belo Horizonte', 8.45, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (17, 'Cliente 17', 31, 'Brasília', 3.96, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (18, 'Cliente 18', 44, 'Fortaleza', 6.61, FALSE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (19, 'Cliente 19', 29, 'Goiânia', 5.00, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (20, 'Cliente 20', 53, 'Brasília', 6.18, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (21, 'Cliente 21', 26, 'Salvador', 9.81, FALSE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (22, 'Cliente 22', 40, 'Goiânia', 2.66, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (23, 'Cliente 23', 48, 'Curitiba', 4.32, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (24, 'Cliente 24', 57, 'Belo Horizonte', 8.94, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (25, 'Cliente 25', 30, 'Rio de Janeiro', 6.53, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (26, 'Cliente 26', 31, 'Brasília', 6.91, FALSE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (27, 'Cliente 27', 44, 'São Paulo', 7.38, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (28, 'Cliente 28', 56, 'Goiânia', 5.27, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (29, 'Cliente 29', 38, 'Curitiba', 4.88, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (30, 'Cliente 30', 41, 'Fortaleza', 6.62, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (31, 'Cliente 31', 29, 'Belo Horizonte', 9.21, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (32, 'Cliente 32', 60, 'Salvador', 3.74, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (33, 'Cliente 33', 35, 'Rio de Janeiro', 6.47, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (34, 'Cliente 34', 45, 'Goiânia', 7.73, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (35, 'Cliente 35', 52, 'Brasília', 5.00, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (36, 'Cliente 36', 48, 'Fortaleza', 2.68, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (37, 'Cliente 37', 33, 'Belo Horizonte', 4.52, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (38, 'Cliente 38', 62, 'São Paulo', 7.94, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (39, 'Cliente 39', 39, 'Salvador', 6.13, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (40, 'Cliente 40', 27, 'Curitiba', 5.67, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (41, 'Cliente 41', 50, 'Brasília', 8.44, FALSE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (42, 'Cliente 42', 34, 'Rio de Janeiro', 3.89, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (43, 'Cliente 43', 59, 'Goiânia', 6.72, FALSE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (44, 'Cliente 44', 36, 'Fortaleza', 7.18, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (45, 'Cliente 45', 46, 'São Paulo', 5.33, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (46, 'Cliente 46', 40, 'Salvador', 4.23, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (47, 'Cliente 47', 55, 'Belo Horizonte', 7.87, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (48, 'Cliente 48', 31, 'Curitiba', 5.00, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (49, 'Cliente 49', 63, 'Rio de Janeiro', 8.26, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (50, 'Cliente 50', 28, 'Brasília', 2.95, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (51, 'Cliente 51', 43, 'Fortaleza', 5.00, FALSE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (52, 'Cliente 52', 39, 'Goiânia', 5.41, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (53, 'Cliente 53', 48, 'Belo Horizonte', 6.78, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (54, 'Cliente 54', 35, 'Salvador', 4.67, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (55, 'Cliente 55', 59, 'São Paulo', 8.55, FALSE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (56, 'Cliente 56', 42, 'Rio de Janeiro', 7.39, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (57, 'Cliente 57', 31, 'Brasília', 2.83, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (58, 'Cliente 58', 66, 'Curitiba', 6.91, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (59, 'Cliente 59', 28, 'Fortaleza', 5.77, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (60, 'Cliente 60', 36, 'Goiânia', 4.88, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (61, 'Cliente 61', 60, 'São Paulo', 7.61, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (62, 'Cliente 62', 30, 'Brasília', 8.46, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (63, 'Cliente 63', 45, 'Rio de Janeiro', 3.98, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (64, 'Cliente 64', 37, 'Belo Horizonte', 6.29, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (65, 'Cliente 65', 53, 'Salvador', 4.21, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (66, 'Cliente 66', 41, 'Fortaleza', 5.53, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (67, 'Cliente 67', 26, 'Curitiba', 8.19, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (68, 'Cliente 68', 47, 'São Paulo', 3.94, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (69, 'Cliente 69', 50, 'Brasília', 7.68, FALSE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (70, 'Cliente 70', 33, 'Belo Horizonte', 5.00, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (71, 'Cliente 71', 40, 'Goiânia', 5.14, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (72, 'Cliente 72', 38, 'Salvador', 8.36, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (73, 'Cliente 73', 61, 'Rio de Janeiro', 3.75, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (74, 'Cliente 74', 28, 'Curitiba', 7.84, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (75, 'Cliente 75', 55, 'Fortaleza', 6.65, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (76, 'Cliente 76', 44, 'São Paulo', 5.92, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (77, 'Cliente 77', 30, 'Goiânia', 7.41, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (78, 'Cliente 78', 58, 'Salvador', 4.86, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (79, 'Cliente 79', 39, 'Brasília', 6.23, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (80, 'Cliente 80', 50, 'Curitiba', 3.68, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (81, 'Cliente 81', 32, 'Fortaleza', 6.74, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (82, 'Cliente 82', 46, 'Rio de Janeiro', 8.14, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (83, 'Cliente 83', 36, 'Belo Horizonte', 7.26, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (84, 'Cliente 84', 42, 'Salvador', 5.33, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (85, 'Cliente 85', 49, 'Curitiba', 5.00, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (86, 'Cliente 86', 60, 'Goiânia', 7.98, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (87, 'Cliente 87', 34, 'Brasília', 3.54, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (88, 'Cliente 88', 56, 'São Paulo', 6.87, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (89, 'Cliente 89', 29, 'Rio de Janeiro', 4.69, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (90, 'Cliente 90', 63, 'Fortaleza', 5.94, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (91, 'Cliente 91', 38, 'Belo Horizonte', 8.51, FALSE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (92, 'Cliente 92', 27, 'Curitiba', 7.33, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (93, 'Cliente 93', 55, 'Goiânia', 3.88, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (94, 'Cliente 94', 40, 'Salvador', 5.00, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (95, 'Cliente 95', 35, 'Rio de Janeiro', 7.76, TRUE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (96, 'Cliente 96', 48, 'São Paulo', 5.19, FALSE, TRUE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (97, 'Cliente 97', 59, 'Belo Horizonte', 4.27, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (98, 'Cliente 98', 33, 'Fortaleza', 6.93, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (99, 'Cliente 99', 45, 'Brasília', 8.67, TRUE, FALSE);
INSERT INTO clientes (cliente_id, nome, idade, cidade, pontuacao_engajamento, assinante_clube, cancelou_assinatura)
VALUES (100, 'Cliente 100', 37, 'Goiânia', 5.36, FALSE, TRUE);

-- =====================
-- PRODUTOS
-- Dados reais da planilha produtos.xlsx
-- IMPORTANTE: NAO possui preco nem estoque
-- =====================

INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (1, 'Vinho 1', 'França', 2020, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (2, 'Vinho 2', 'Brasil', 2018, 'Sauvignon Blanc');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (3, 'Vinho 3', 'Chile', 2021, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (4, 'Vinho 4', 'Itália', 2022, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (5, 'Vinho 5', 'Portugal', 2019, 'Malbec');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (6, 'Vinho 6', 'Espanha', 2021, 'Syrah');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (7, 'Vinho 7', 'Argentina', 2023, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (8, 'Vinho 8', 'África do Sul', 2020, 'Tempranillo');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (9, 'Vinho 9', 'Chile', 2022, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (10, 'Vinho 10', 'França', 2017, 'Syrah');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (11, 'Vinho 11', 'Brasil', 2021, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (12, 'Vinho 12', 'Itália', 2023, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (13, 'Vinho 13', 'Espanha', 2020, 'Malbec');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (14, 'Vinho 14', 'Argentina', 2019, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (15, 'Vinho 15', 'Portugal', 2021, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (16, 'Vinho 16', 'França', 2020, 'Sauvignon Blanc');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (17, 'Vinho 17', 'África do Sul', 2022, 'Syrah');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (18, 'Vinho 18', 'Chile', 2021, 'Tempranillo');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (19, 'Vinho 19', 'Brasil', 2020, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (20, 'Vinho 20', 'Itália', 2018, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (21, 'Vinho 21', 'Portugal', 2019, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (22, 'Vinho 22', 'França', 2022, 'Malbec');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (23, 'Vinho 23', 'Espanha', 2023, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (24, 'Vinho 24', 'Argentina', 2021, 'Tempranillo');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (25, 'Vinho 25', 'África do Sul', 2020, 'Syrah');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (26, 'Vinho 26', 'Chile', 2023, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (27, 'Vinho 27', 'Brasil', 2019, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (28, 'Vinho 28', 'Itália', 2022, 'Sauvignon Blanc');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (29, 'Vinho 29', 'Portugal', 2021, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (30, 'Vinho 30', 'França', 2020, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (31, 'Vinho 31', 'Espanha', 2018, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (32, 'Vinho 32', 'Argentina', 2022, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (33, 'Vinho 33', 'África do Sul', 2019, 'Sauvignon Blanc');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (34, 'Vinho 34', 'Chile', 2023, 'Malbec');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (35, 'Vinho 35', 'Brasil', 2020, 'Syrah');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (36, 'Vinho 36', 'Itália', 2021, 'Tempranillo');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (37, 'Vinho 37', 'Portugal', 2018, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (38, 'Vinho 38', 'França', 2022, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (39, 'Vinho 39', 'Espanha', 2019, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (40, 'Vinho 40', 'Argentina', 2021, 'Syrah');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (41, 'Vinho 41', 'África do Sul', 2020, 'Sauvignon Blanc');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (42, 'Vinho 42', 'Chile', 2022, 'Tempranillo');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (43, 'Vinho 43', 'Brasil', 2023, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (44, 'Vinho 44', 'Itália', 2019, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (45, 'Vinho 45', 'Portugal', 2020, 'Malbec');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (46, 'Vinho 46', 'França', 2021, 'Sauvignon Blanc');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (47, 'Vinho 47', 'Espanha', 2022, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (48, 'Vinho 48', 'Argentina', 2023, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (49, 'Vinho 49', 'África do Sul', 2018, 'Syrah');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (50, 'Vinho 50', 'Chile', 2017, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (51, 'Vinho 51', 'Brasil', 2019, 'Tempranillo');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (52, 'Vinho 52', 'Itália', 2020, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (53, 'Vinho 53', 'Portugal', 2023, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (54, 'Vinho 54', 'França', 2021, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (55, 'Vinho 55', 'Espanha', 2020, 'Malbec');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (56, 'Vinho 56', 'Argentina', 2022, 'Sauvignon Blanc');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (57, 'Vinho 57', 'África do Sul', 2019, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (58, 'Vinho 58', 'Chile', 2023, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (59, 'Vinho 59', 'Brasil', 2021, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (60, 'Vinho 60', 'Itália', 2018, 'Syrah');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (61, 'Vinho 61', 'Portugal', 2019, 'Tempranillo');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (62, 'Vinho 62', 'França', 2022, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (63, 'Vinho 63', 'Espanha', 2020, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (64, 'Vinho 64', 'Argentina', 2021, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (65, 'Vinho 65', 'África do Sul', 2017, 'Sauvignon Blanc');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (66, 'Vinho 66', 'Chile', 2019, 'Malbec');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (67, 'Vinho 67', 'Brasil', 2020, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (68, 'Vinho 68', 'Itália', 2022, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (69, 'Vinho 69', 'Portugal', 2021, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (70, 'Vinho 70', 'França', 2023, 'Tempranillo');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (71, 'Vinho 71', 'Espanha', 2018, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (72, 'Vinho 72', 'Argentina', 2019, 'Sauvignon Blanc');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (73, 'Vinho 73', 'África do Sul', 2021, 'Malbec');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (74, 'Vinho 74', 'Chile', 2020, 'Syrah');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (75, 'Vinho 75', 'Brasil', 2019, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (76, 'Vinho 76', 'Itália', 2023, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (77, 'Vinho 77', 'Portugal', 2018, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (78, 'Vinho 78', 'França', 2021, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (79, 'Vinho 79', 'Espanha', 2022, 'Malbec');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (80, 'Vinho 80', 'Argentina', 2020, 'Sauvignon Blanc');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (81, 'Vinho 81', 'África do Sul', 2023, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (82, 'Vinho 82', 'Chile', 2019, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (83, 'Vinho 83', 'Brasil', 2021, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (84, 'Vinho 84', 'Itália', 2022, 'Tempranillo');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (85, 'Vinho 85', 'Portugal', 2020, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (86, 'Vinho 86', 'França', 2019, 'Sauvignon Blanc');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (87, 'Vinho 87', 'Espanha', 2023, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (88, 'Vinho 88', 'Argentina', 2021, 'Malbec');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (89, 'Vinho 89', 'África do Sul', 2018, 'Syrah');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (90, 'Vinho 90', 'Chile', 2020, 'Merlot');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (91, 'Vinho 91', 'Brasil', 2023, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (92, 'Vinho 92', 'Itália', 2019, 'Tempranillo');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (93, 'Vinho 93', 'Portugal', 2021, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (94, 'Vinho 94', 'França', 2022, 'Cabernet Sauvignon');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (95, 'Vinho 95', 'Espanha', 2020, 'Malbec');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (96, 'Vinho 96', 'Argentina', 2023, 'Sauvignon Blanc');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (97, 'Vinho 97', 'África do Sul', 2020, 'Syrah');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (98, 'Vinho 98', 'Chile', 2019, 'Pinot Noir');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (99, 'Vinho 99', 'Brasil', 2022, 'Chardonnay');
INSERT INTO produtos (produto_id, nome, pais, safra, tipo_uva)
VALUES (100, 'Vinho 100', 'Itália', 2021, 'Tempranillo');

-- =====================
-- COMPRAS
-- Dados reais da planilha Compras1.xlsx
-- O campo 'valor' contem o preco real da transacao
-- =====================

INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (1, 13, 47, 84.79, 1, '2023-01-19');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (2, 11, 67, 358.65, 2, '2023-03-27');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (3, 21, 94, 93.28, 5, '2023-08-14');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (4, 52, 11, 66.31, 4, '2023-02-10');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (5, 29, 20, 241.08, 1, '2023-07-22');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (6, 61, 82, 278.11, 3, '2023-06-01');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (7, 28, 18, 123.87, 2, '2023-12-26');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (8, 7, 66, 234.00, 2, '2023-04-12');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (9, 19, 40, 299.31, 1, '2023-10-03');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (10, 10, 34, 310.92, 4, '2023-09-05');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (11, 16, 8, 190.38, 2, '2023-11-15');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (12, 18, 57, 124.72, 1, '2023-05-08');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (13, 14, 15, 227.69, 3, '2023-03-20');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (14, 77, 33, 62.90, 6, '2023-12-08');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (15, 20, 96, 146.44, 1, '2023-06-28');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (16, 54, 17, 161.35, 2, '2023-08-30');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (17, 84, 87, 211.08, 5, '2023-02-03');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (18, 11, 91, 92.55, 4, '2023-10-12');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (19, 27, 44, 288.18, 3, '2023-07-01');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (20, 31, 69, 133.39, 3, '2023-11-04');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (21, 45, 4, 129.67, 1, '2023-03-06');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (22, 56, 22, 232.61, 1, '2023-05-18');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (23, 96, 86, 186.12, 2, '2023-01-27');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (24, 95, 3, 173.06, 4, '2023-09-09');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (25, 41, 3, 258.96, 5, '2023-06-15');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (26, 60, 52, 101.44, 1, '2023-08-20');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (27, 89, 78, 113.11, 2, '2023-10-24');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (28, 43, 46, 386.50, 3, '2023-07-07');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (29, 30, 33, 243.35, 2, '2023-06-06');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (30, 36, 9, 177.07, 3, '2023-11-23');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (31, 87, 31, 102.69, 1, '2023-05-31');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (32, 74, 81, 287.78, 5, '2023-12-04');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (33, 58, 12, 264.47, 1, '2023-04-05');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (34, 8, 83, 339.64, 3, '2023-02-14');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (35, 34, 99, 96.80, 1, '2023-03-29');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (36, 14, 60, 192.73, 1, '2023-09-21');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (37, 20, 100, 94.99, 6, '2023-01-12');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (38, 82, 69, 295.59, 3, '2023-06-19');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (39, 62, 38, 258.39, 4, '2023-08-22');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (40, 29, 85, 134.12, 2, '2023-03-07');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (41, 92, 92, 97.13, 2, '2023-09-02');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (42, 25, 75, 390.38, 1, '2023-02-20');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (43, 8, 89, 111.44, 4, '2023-07-13');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (44, 83, 77, 71.87, 2, '2023-05-24');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (45, 53, 55, 124.73, 4, '2023-06-08');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (46, 27, 87, 191.41, 2, '2023-10-18');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (47, 31, 54, 241.70, 5, '2023-12-22');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (48, 97, 37, 160.33, 2, '2023-01-06');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (49, 5, 64, 108.27, 3, '2023-04-14');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (50, 71, 16, 313.02, 1, '2023-11-28');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (51, 1, 24, 156.79, 1, '2023-07-19');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (52, 62, 10, 226.30, 3, '2023-02-01');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (53, 89, 63, 175.94, 2, '2023-03-13');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (54, 10, 57, 242.88, 4, '2023-06-03');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (55, 83, 26, 85.63, 1, '2023-05-05');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (56, 46, 45, 298.97, 3, '2023-08-27');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (57, 44, 82, 234.47, 2, '2023-09-25');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (58, 72, 51, 118.15, 1, '2023-11-07');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (59, 32, 68, 267.83, 4, '2023-03-02');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (60, 76, 59, 368.23, 5, '2023-12-11');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (61, 3, 47, 70.84, 2, '2023-01-23');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (62, 93, 79, 81.49, 2, '2023-07-02');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (63, 97, 35, 103.21, 3, '2023-04-10');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (64, 80, 23, 174.57, 4, '2023-02-09');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (65, 26, 87, 266.73, 1, '2023-06-13');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (66, 96, 89, 313.44, 2, '2023-10-26');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (67, 57, 95, 271.67, 3, '2023-03-15');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (68, 59, 78, 90.02, 6, '2023-12-06');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (69, 40, 36, 112.65, 1, '2023-09-17');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (70, 68, 71, 78.35, 2, '2023-11-18');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (71, 90, 91, 84.91, 3, '2023-08-10');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (72, 41, 72, 339.71, 2, '2023-05-12');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (73, 78, 28, 198.67, 1, '2023-07-24');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (74, 14, 60, 132.05, 5, '2023-06-26');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (75, 99, 97, 237.40, 1, '2023-04-07');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (76, 66, 100, 254.73, 2, '2023-05-28');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (77, 53, 16, 159.65, 1, '2023-09-01');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (78, 65, 60, 126.18, 2, '2023-07-09');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (79, 20, 49, 187.44, 3, '2023-02-17');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (80, 5, 21, 308.56, 4, '2023-08-29');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (81, 90, 33, 94.76, 1, '2023-04-03');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (82, 54, 56, 271.36, 5, '2023-11-10');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (83, 36, 70, 109.07, 2, '2023-12-20');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (84, 79, 26, 195.78, 3, '2023-01-30');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (85, 13, 38, 317.99, 2, '2023-03-18');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (86, 35, 76, 221.88, 4, '2023-06-22');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (87, 22, 39, 258.19, 2, '2023-07-27');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (88, 31, 67, 161.64, 1, '2023-10-08');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (89, 14, 12, 100.93, 3, '2023-02-12');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (90, 75, 32, 154.82, 1, '2023-05-02');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (91, 46, 85, 295.12, 2, '2023-06-18');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (92, 81, 20, 243.40, 2, '2023-08-05');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (93, 2, 29, 210.55, 3, '2023-09-14');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (94, 22, 4, 88.79, 4, '2023-11-20');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (95, 100, 40, 123.33, 1, '2023-01-14');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (96, 43, 44, 219.80, 2, '2023-03-04');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (97, 25, 66, 164.96, 5, '2023-04-25');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (98, 9, 55, 132.79, 2, '2023-12-01');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (99, 91, 90, 93.87, 1, '2023-07-06');
INSERT INTO compras (compra_id, cliente_id, produto_id, valor, quantidade, data_compra)
VALUES (100, 14, 19, 243.77, 3, '2023-10-30');
