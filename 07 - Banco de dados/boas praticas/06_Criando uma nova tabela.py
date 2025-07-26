
# Faze 5 criando uma nova tabela detro do nosso banco de dados , utilizando o "cursor" para isso ok

# https://docs.python.org/pt-br/3/library/sqlite3.html 
# "sqlite3 —- interface DB-API 2.0 interface para bancos de dados SQLite"

import sqlite3                              # importando o sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# conexao = sqlite3.connect(ROOT_PATH / "meu_washbanco.db")    # trocando o nome do nosso db "clientes_dio.db" para "meu_washbanco.db" e delete o "clientes_dio.db" ok
conexao = sqlite3.connect(ROOT_PATH / "meu_banco_2.sqlite")    # trocando a exptencao do nosso db "meu_washbanco.db" para "meu_washbanco.sqlite" por Causa do plugim que nao reconhece o .db ok


cursor = conexao.cursor()


# cursor.execute("create table clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150), telefone VARCHAR(12), funcao VARCHAR(20))")
