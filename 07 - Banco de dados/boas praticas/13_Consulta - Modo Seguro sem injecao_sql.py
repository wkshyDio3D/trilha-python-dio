

import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco_2.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


id_cliente = input(" Informe o id do cliente: ")
# cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")
cursor.execute(f"SELECT * FROM clientes WHERE id=?", (id_cliente,))

cliente = cursor.fetchone()
print(dict(cliente))

# Informe o id do cliente: 1 OR 1=1;

# >>> {'id': 1, 'nome': 'Wash', 'email': 'wash@gmail.com', 'telefone': '397356957', 'funcao': 'Python_Program'}

id_cliente = input(" Informe o id do cliente: ")
# cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")
cursor.execute(f"SELECT * FROM clientes WHERE id=?", (id_cliente,))

clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))

# Informe o id do cliente: 3
# {'id': 3, 'nome': 'well', 'email': 'well@gmail.com', 'telefone': '97655234', 'funcao': 'Java_Program'}



# cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}") <<<== Modo Errado...

# busca com injecao de sql... Codigo corrigido Sem Vazamento de dados nao retorna nada.
# cursor.execute(f"SELECT * FROM clientes WHERE id=?", (id_cliente,)) <<<== Modo Correto

# Informe o id do cliente: 1 OR 1=1;    <<<== injetando Sql.
# Nao Retorna nada com a injecao de sql...
# PS C:\Users\warp\Documents\GitHub\trilha-python-dio> 