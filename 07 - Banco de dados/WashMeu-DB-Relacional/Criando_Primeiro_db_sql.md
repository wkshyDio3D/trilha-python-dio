
https://docs.python.org/pt-br/3/library/sqlite3.html

# 1 Fase ===== criando o banco de dados ===== "clientes_dio.db" no "diretorio Raiz"  =====

# import sqlite3                              # importando o sqlite3

# sqlite3.connect("clientes_dio.db")          # Criando o Banco de dados "*.db".

# conexao = sqlite3.connect("clientes_dio.db")   # Aqui devolve a conecao com o Banco de dados "*.db".

# print(conexao)

# RUM ==>> rodar o codigo.

# 2 Fase == colocando o banco de dados criado --"clientes_dio.db" na mesma "pasta" =====

import sqlite3                              # importando o sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

# sqlite3.connect("clientes_dio.db")          # Criando o Banco de dados "*.db".

conexao = sqlite3.connect(ROOT_PATH / "clientes_dio.db")   # Aqui devolve a conecao com o Banco de dados "*.db". na mesma "pasta"

print(conexao)

# RUM ==>> rodar o codigo.

# Procurar e instalar uma instencao para abrir o "sqlite3". De preferencia utilize o "SqLite Viewer" - by Florian Klampfer - qwtel.com

# Pronto Banco de dados Criado 
-- cria um novo banco de dados.
CREATE DADABASE LOJA;

--cria uma tabela para armazenar informacoes de produtos.
CREATE TABLE produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), preco DECIMAL);

-- inclui um novo produto.
INSERT INTO produtos (nome, preco) VALUES ('Curso de Python', 250.00);

-- lista todos os produtos.
SELECT * FROM produtos;

-- Atualiza o produto com o id informado.
UPDATE produtos SET nome='Curso de Python para iniciantes' WHERE id = 1;

-- Exclui o produto com o id informado.
DELETE FROM produtos WHERE id = 1;