# mudando o nome do db de ("clientes_dio.db") para  ("meu_banco.db")
# obs ==>> o Sqlite3 ao inves de usar o ".db"  usa a extencao ".sqlite".
# Entao vamos mudar o nome do nosso novo banco de dados ("meu_banco.db") para ("meu_banco.sqlite").

import sqlite3                              # importando o sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

# sqlite3.connect("clientes_dio.db")          # Criando o Banco de dados "*.db".

conexao = sqlite3.connect(ROOT_PATH / "clientes_dio.db")   # Aqui devolve a conecao com o Banco de dados "*.db". na mesma "pasta"

conexao = sqlite3.connect(ROOT_PATH / "meu_washbanco.db")    # trocando o nome do nosso db "clientes_dio.db" para "meu_washbanco.db" e delete o "clientes_dio.db" ok

# o cursor e o objeto que prescisamos recuperar para consegur executar comandos no nosso banco de dados.
# cursor = conexao.cursor()   # recuperendo o cursor que esta dentro da conexao.


# https://docs.python.org/pt-br/3/library/sqlite3.html 
# "sqlite3 —- interface DB-API 2.0 interface para bancos de dados SQLite"
# print(conexao)

