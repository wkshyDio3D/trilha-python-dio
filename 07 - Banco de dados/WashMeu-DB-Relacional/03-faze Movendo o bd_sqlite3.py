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