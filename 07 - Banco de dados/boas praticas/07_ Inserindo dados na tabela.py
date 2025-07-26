
# Inserindo dados na nossa tabela


import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco_2.sqlite")    
cursor = conexao.cursor()

# como a nossa tabela ja esta criada deixe a linha abaixo comentada ou crie uma execao para pular se ja existir.
# cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150), telefone VARCHAR(12), funcao VARCHAR(20))")

# Aqui agora vamos inserir dados na nossa tabela 

# data = ("Wash", "wash@gmail.com", 397356957, "Python_Program")
# data = ("well", "well@gmail.com", 97655234, "Java_Program")
data = ("will", "will@gmail.com", 89873545, "Html_Program")
# data = ("del", "delete@gmail.com", 97655234, "Deletando_Registro")


cursor.execute("INSERT INTO clientes (nome, email, telefone, funcao) VALUES (?, ?, ?, ?)", data)
# Aqui finalizamos de inserir dados na nossa tabela 

conexao.commit()  # importante para salvar as alterações no banco
# conexao.close()

