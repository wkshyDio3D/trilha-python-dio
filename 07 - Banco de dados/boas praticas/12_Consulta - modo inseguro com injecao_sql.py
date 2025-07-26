

import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco_2.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


id_cliente = input(" Informe o id do cliente A: ")
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")

cliente = cursor.fetchone()
print(dict(cliente))

# Informe o id do cliente: 1 OR 1=1;

# >>> {'id': 1, 'nome': 'Wash', 'email': 'wash@gmail.com', 'telefone': '397356957', 'funcao': 'Python_Program'}

id_cliente = input(" Informe o id do cliente B: ")
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")


clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))

# busca sem injecao de sql...
# Informe o id do cliente: 3
# {'id': 3, 'nome': 'well', 'email': 'well@gmail.com', 'telefone': '97655234', 'funcao': 'Java_Program'}


# busca com injecao de sql... falha grave no cod. com vazamento de dados
# cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}") <<<== Modo Errado...

# Informe o id do cliente: 1 OR 1=1;
# {'id': 1, 'nome': 'Wash', 'email': 'wash@gmail.com', 'telefone': '397356957', 'funcao': 'Python_Program'}    
# {'id': 2, 'nome': 'del', 'email': 'delete@gmail.com', 'telefone': '97655234', 'funcao': 'Deletando_Registro'}
# {'id': 3, 'nome': 'well', 'email': 'well@gmail.com', 'telefone': '97655234', 'funcao': 'Java_Program'}       
# {'id': 4, 'nome': 'will', 'email': 'will@gmail.com', 'telefone': '89873545', 'funcao': 'Html_Program'}   