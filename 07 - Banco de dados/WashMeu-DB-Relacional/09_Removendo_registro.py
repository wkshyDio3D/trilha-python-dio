
# Removendo Registro com Delete do sql.


import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_washbanco.sqlite")    
cursor = conexao.cursor()

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

# atualizar_registro(conexao, cursor, "Mari_Html", "MarHt@gmail.com", 3)
# Aqui ao inves chamar a funcao "atualizar_registro" vamos chamar "excluir_registro".

excluir_registro(conexao, cursor, 4) # Aqui colocamos a "conexao", o "cursor", e o "id". que sera excluido.


# atualizar_registro(conexao, cursor, "Washing Python", "washpy@gmail.com", 1)
# atualizar_registro(conexao, cursor, "Welling_Java", "wellJv@gmail.com", 2)


# data = ("Wash", "wash@gmail.com", 397356957, "Python_Program")
# data = ("well", "well@gmail.com", 97655234, "Java_Program")
# data = ("will", "will@gmail.com", 89873545, "Html_Program")
# cursor.execute("INSERT INTO clientes (nome, email, telefone, funcao) VALUES (?, ?, ?, ?)", data)
# Aqui finalizamos de inserir dados na nossa tabela 

# conexao.commit()  # importante para salvar as alterações no banco
# conexao.close()