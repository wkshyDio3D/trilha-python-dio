import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Informe o id do cliente: ")

# Essa Aqui e a forma Incorreta de buscar dados dos clientes sem Protecao e vazamentos de dados 
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")

# Essa Aqui e a forma Correta de buscar dados dos clientes com Protecao e sem Vazamentos de dados .
# cursor.execute("SELECT * FROM clientes WHERE id=?", (id_cliente,))

clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))
