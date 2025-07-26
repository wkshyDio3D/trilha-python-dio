
#
import sqlite3                              # importando o sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco_2.sqlite")    # trocando o nome do nosso db "clientes_dio.db" para "meu_washbanco.db" e delete o "clientes_dio.db" ok

cursor = conexao.cursor()



