

# 11 - Consultando Registros individuais com metodo ==>>  "fetchone()" .

# conexao.commit()  # importante para salvar as alterações no banco
# conexao.close()

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

def inserir_muitos(conexao, cursor, dados):  # aqui precisamos apenas do "dados".
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conexao.commit()

# dados = [
#    ("kierstin", "kierst_coy@gmail.com"),
#    ("Holartt", "lyart@gmail.com"),
#    ("yeniCha", "fer_com@gmail.com"),
#]

# inserir_muitos(conexao, cursor, dados)

# ------- Recuperando informacoes do "id" informado ---------------
def recuperar_cliente(cursor, id):  # obs apenas a ultima linha sera respondida ok as outras dixe comentadas ok 
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))  # Retornando "*" todas informacoes do "id".
    cursor.execute("SELECT email FROM clientes WHERE id=?", (id,))  # Retornando "email" do "id".
    cursor.execute("SELECT id, email FROM clientes WHERE id=?", (id,))  # Retornando "id" e "email" do "id".
    cursor.execute("SELECT nome FROM clientes WHERE id=?", (id,))  # Retornando "nome" do "id".
    cursor.execute("SELECT id, nome FROM clientes WHERE id=?", (id,))  # Retornando "id" e "nome" do "id".
    cursor.execute("SELECT nome, telefone FROM clientes WHERE id=?", (id,))  # Retornando "nome" e "Telefone".
    cursor.execute("SELECT id, nome, telefone FROM clientes WHERE id=?", (id,))  # Retornando "id", "nome" e "Telefone".



    return cursor.fetchone()

# cliente = recuperar_cliente(cursor, 3)  # Retornando o "id" Especificado..
# print(cliente)                          # >>> ((3, 'may_ile', '97655234')

# cliente = recuperar_cliente(cursor, 1)  # Retornando o "id" Especificado..
# print(cliente)                          # >>> (1, 'man_flo', '397356957')

cliente = recuperar_cliente(cursor, 3)  # Retornando o "id" Especificado..
print(cliente)                          # >>> ((3, 'may_ile', '97655234')

cliente = recuperar_cliente(cursor, 1)  # Retornando o "id" Especificado..
print(cliente)                          # (1, 'man_flo', '397356957')

cliente = recuperar_cliente(cursor, 7)  # Retornando o "id" Especificado..
print(cliente)                          # >>> (7, 'yeniCha', None)

cliente = recuperar_cliente(cursor, 5)  # Retornando o "id" Especificado..
print(cliente)                          # >>> (5, 'kierstin', None)
