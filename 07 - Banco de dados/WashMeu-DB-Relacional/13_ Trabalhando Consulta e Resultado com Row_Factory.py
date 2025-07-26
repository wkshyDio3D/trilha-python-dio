
# Trabalhando com resultados de Consulta . 
# Os resultados sao retornados comotuplas por padrao. se a tupla nao atender as 
#  nescecidades usamos a classe "sqlite3.Row" ou uma "row_Factory" customizada.

# Aqui vamos trocar o "cursor = conexao.cursor()" por "cursor.row_factory"
# anterior ===>> cursor = conexao.cursor()

# Atual ==>>
# cursor.row_factory = sqlite3.Row
# cursor.execute('SELECT * FROM minha_tabela WHERE id = 1')
# result = cursor.fetchone()
# print(dict(result))  # Aqui converte para um Dicionario.


# 1 - Consultando Registros usando a classe "sqlite3.Row" ou uma  "Row_factory" Customizada.


import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_washbanco.sqlite")    
cursor = conexao.cursor()
# cursor.row_factory = sqlite3.Row    # Tornando a "row_factory" como padao.

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

# 1 - Consultando Registros com o Metodo "fetchall()" que retorna uma lista .

# inserir_muitos(conexao, cursor, dados)

# ------- Recuperando informacoes do "id" ==>>informado ---------------
# def recuperar_cliente(cursor, id):  # obs apenas a ultima linha sera respondida ok as outras dixe comentadas ok 
  #  cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))  # Retornando "*" todas informacoes do "id".
  #  return cursor.fetchone()

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


# ------- Recuperando informacoes do "id" informado --------------
# cliente = recuperar_cliente(cursor, 2)
# print(cliente)



# ------ recuperar lista de clientes -----------
clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)

# ------- Recuperando informacoes do "id" informado ==>> Usando Row_Factory--------------
# cliente = recuperar_cliente(cursor, 2)
# print(cliente)

# retornos do pedido ... 
# >>> (1, 'man_flo', 'dy_flores@gmail.com', '397356957', 'Python_Program')
# >>> (2, 'le_got', 'ah got@gmail.com', '89873545', 'Html_Program')  
# >>> (2, 'le_got', 'ah got@gmail.com', '89873545', 'Html_Program')  
# >>> (3, 'may_ile', 'ara_ile@gmail.com', '97655234', 'Java_Program')
# >>> (5, 'kierstin', 'kierst_coy@gmail.com', None, None)
# >>> (6, 'Holartt', 'lyart@gmail.com', None, None)
# >>> (7, 'yeniCha', 'fer_com@gmail.com', None, None)
# >>> <sqlite3.Row object at 0x000002A9B1CECA00>

# ------- Recuperando informacoes do "id" informado ==>> Usando Row_Factory--------------
# cliente = recuperar_cliente(cursor, 2)
# print(dict(cliente))    # convertendo em um dicionario.

# >>> (1, 'man_flo', 'dy_flores@gmail.com', '397356957', 'Python_Program')
# >>> (2, 'le_got', 'ah got@gmail.com', '89873545', 'Html_Program')
# >>> (3, 'may_ile', 'ara_ile@gmail.com', '97655234', 'Java_Program')
# >>> (5, 'kierstin', 'kierst_coy@gmail.com', None, None)
# >>> (6, 'Holartt', 'lyart@gmail.com', None, None)
# >>> (7, 'yeniCha', 'fer_com@gmail.com', None, None)
# >>> {'id': 2, 'nome': 'le_got', 'email': 'ah got@gmail.com', 'telefone': '89873545', 'funcao': 'Html_Program'}

cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))    # convertendo em um dicionario.
# print(cliente.id)       # Forma errada vai dar erro...
print(cliente["id"], cliente["nome"], cliente["email"])

# Saidas # >>>
# >>> 1, 'man_flo', 'dy_flores@gmail.com', '397356957', 'Python_Program')
# >>> (2, 'le_got', 'ah got@gmail.com', '89873545', 'Html_Program')
# >>> (3, 'may_ile', 'ara_ile@gmail.com', '97655234', 'Java_Program')
# >>> (5, 'kierstin', 'kierst_coy@gmail.com', None, None)
# >>> (6, 'Holartt', 'lyart@gmail.com', None, None)
# >>> (7, 'yeniCha', 'fer_com@gmail.com', None, None)
# >>> {'id': 2, 'nome': 'le_got', 'email': 'ah got@gmail.com', 'telefone': '89873545', 'funcao': 'Html_Program'}
# >>> 2 le_got ah got@gmail.com