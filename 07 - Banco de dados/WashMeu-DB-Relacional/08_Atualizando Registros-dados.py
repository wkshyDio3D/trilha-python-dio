

# 07 - Atualizando Registros ou dados na nossa tabela


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

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email,id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE ID=?;", data)
    conexao.commit()

atualizar_registro(conexao, cursor, "man_flo", "dy_flores@gmail.com", 1)
# atualizar_registro(conexao, cursor, "le_got", "ah got@gmail.com", 2)
# atualizar_registro(conexao, cursor, "may_ile", "ara_ile@gmail.com", 3)

# atualizar_registro(conexao, cursor, "Del_delete", "del_delete@gmail.com", 4)

# data = ("Wash", "wash@gmail.com", 397356957, "Python_Program")
# data = ("well", "well@gmail.com", 97655234, "Java_Program")
# data = ("will", "will@gmail.com", 89873545, "Html_Program")
# cursor.execute("INSERT INTO clientes (nome, email, telefone, funcao) VALUES (?, ?, ?, ?)", data)
# Aqui finalizamos de inserir dados na nossa tabela 

# conexao.commit()  # importante para salvar as alterações no banco
# conexao.close()
