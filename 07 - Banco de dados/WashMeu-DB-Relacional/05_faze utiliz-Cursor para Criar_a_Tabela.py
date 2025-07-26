
# Faze 5 criando uma nova tabela detro do nosso banco de dados , utilizando o "cursor" para isso ok

# https://docs.python.org/pt-br/3/library/sqlite3.html 
# "sqlite3 —- interface DB-API 2.0 interface para bancos de dados SQLite"

import sqlite3                              # importando o sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_washbanco.db")    # trocando o nome do nosso db "clientes_dio.db" para "meu_washbanco.db" e delete o "clientes_dio.db" ok

# o cursor e o objeto que prescisamos recuperar para consegur executar comandos no nosso banco de dados.
# cursor = conexao.cursor()   # recuperendo o cursor que esta dentro da conexao.

# utilizando o "cursor" para criar a tabela
# CREATE TABLE produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), preco DECIMAL);
cursor = conexao.cursor()

# Agora que temos uma conexão com o banco de dados e um cursor, podemos criar uma tabela
#  de banco de dados movie com colunas para título, ano de lançamento e pontuação etc...

