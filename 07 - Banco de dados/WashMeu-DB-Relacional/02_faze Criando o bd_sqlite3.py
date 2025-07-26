
# 1 Fase ===== criando o banco de dados ===== "clientes_dio.db" no "diretorio Raiz"  =====

import sqlite3                              # importando o sqlite3

sqlite3.connect("clientes_dio.db")          # Criando o Banco de dados "*.db".

conexao = sqlite3.connect("clientes_dio.db")   # Aqui devolve a conecao com o Banco de dados "*.db".

print(conexao)

# RUM ==>> rodar o codigo.

