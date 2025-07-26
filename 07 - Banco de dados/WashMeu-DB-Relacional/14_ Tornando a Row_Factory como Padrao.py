
# 1 - Consultando Registros usando a classe "sqlite3.Row" ou uma  "Row_factory" Customizada.
# Tornando a "row_factory" como padao.

import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_washbanco.sqlite")    
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row    # Tornando a "row_factory" como padao.

# Aqui agora vamos Atualizar Registros ou dado na tabela .
def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, " \
        "nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email): ## Aqui vamos inserir apenas "nome e email".
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):   # Aqui vamos atualizar apenas "nome e email".
    data = (nome, email,id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE ID=?;", data)
    conexao.commit()

def excluir_registro(conexao, cursor, id):  # aqui precisamos apenas do "id,".
    data = (id,)    # Aqui tem que colocar a virgula ",". 
    # cursor.execute("UPDATE clientes SET nome=?, email=? WHERE ID=?;", data)
    cursor.execute("DELETE FROM clientes WHERE ID=?;", data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):  # aqui precisamos apenas do "dados".
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conexao.commit()


# ------- Recuperando informacoes do "id" ==>> usando o metodo Row_Factory ---------------
def recuperar_cliente(cursor, id):  # obs apenas a ultima linha sera respondida ok as outras dixe comentadas ok 
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))  # Retornando "*" todas informacoes do "id".
    return cursor.fetchone()

# ------ recuperar lista de clientes -----------
def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes;")     # Aqui esta pedindo para retornar todos os clientes.
    # return cursor.execute("SELECT * FROM clientes ORDER BY nome;")  # Ordenando pelo "nome".
    # return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")  # Ordenando por nome decrecente.
    # return cursor.execute("SELECT * FROM clientes ORDER BY email;")  # Ordenando pelo "email".
    # return cursor.execute("SELECT * FROM clientes ORDER BY telefone;")  # Ordenando pelo "telefone".
    # return cursor.execute("SELECT * FROM clientes ORDER BY funcao;")  # Ordenando pelo "funcao".
    # return cursor.execute("SELECT * FROM clientes ORDER BY nome, telefone, email;")  # Ordenando por nome, telefone, email.


# Usando a Row_factory como Padrao...
# ------ recuperar lista de clientes -----------
clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))    # Usando a Row_factory como padrao...



cliente = recuperar_cliente(cursor, 2)
print(dict(cliente)) 
print(cliente["id"], cliente["nome"], cliente["email"])

# >>> ]633;C{'id': 1, 'nome': 'man_flo', 'email': 'dy_flores@gmail.com', 'telefone': '397356957', 'funcao': 'Python_Program'}
# >>> {'id': 2, 'nome': 'le_got', 'email': 'ah got@gmail.com', 'telefone': '89873545', 'funcao': 'Html_Program'}  
# >>> {'id': 3, 'nome': 'may_ile', 'email': 'ara_ile@gmail.com', 'telefone': '97655234', 'funcao': 'Java_Program'}
# >>> {'id': 5, 'nome': 'kierstin', 'email': 'kierst_coy@gmail.com', 'telefone': None, 'funcao': None}
# >>> {'id': 6, 'nome': 'Holartt', 'email': 'lyart@gmail.com', 'telefone': None, 'funcao': None}
# >>> {'id': 7, 'nome': 'yeniCha', 'email': 'fer_com@gmail.com', 'telefone': None, 'funcao': None}
# >>> {'id': 2, 'nome': 'le_got', 'email': 'ah got@gmail.com', 'telefone': '89873545', 'funcao': 'Html_Program'}  
# >>> 2 le_got ah got@gmail.com

# escrevendo uma linha de boas vindas 

print(f' Seja bem Vimdo ao Sistema cliente id ==>> {cliente["id"]}')

print(f' Seja bem Vimdo ao Sistema cliente Sr-a {cliente["nome"]}')

print(f' Seja bem Vimdo ao Sistema Master Program ==>> {cliente["funcao"]}')

print(f' Seja bem Vimdo ao Sistema cliente email ==>> {cliente["email"]}')