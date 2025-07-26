import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

# Modo 01 ==>> Melhor Modo de Gerenciar as transacoes

try:
    cursor.execute("DELETE FROM clientes WHERE id = 18;")
    conexao.commit()

    # cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Teste 1", "teste1@gmail.com"))
    # conexao.commit()
    # cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2, "Teste 1", "teste1@gmail.com"))
    # conexao.commit()

    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Teste 3", "teste3@gmail.com"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2, "Teste 4", "teste4@gmail.com"))
    cursor.execute("DELETE FROM clientes WHERE id = 8;")
    conexao.commit()

    # cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Teste 3", "teste3@gmail.com"))
    # cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2, "Teste 4", "teste4@gmail.com"))
    # conexao.commit()
except Exception as exc:
    print(f"Ops! 'A' um erro ocorreu ! {exc}")   # "exc = excesao"
    conexao.rollback()


# Gerenciamento de Transacoes.

# A DB API Nos permite Gerenciar Transacoes, Isto e crucial para manter a integridade dos Nossos dados.

# Exemplo de Codigo Para Gerenciar Transacoes....

# Modo 02 Segunda opcao de  Gerenciar as transacoes

# with sqlite3.connect(ROOT_PATH / "meu_banco.sqlite") as conexao:
        # Criar as Excecoes Aqui
try:
    cursor.execute("DELETE FROM clientes WHERE id = 8;")
    conexao.commit()

    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Teste 3", "teste3@gmail.com"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2, "Teste 4", "teste4@gmail.com"))
    conexao.commit()
except Exception as exc:
    print(f"Ops! 'B' um erro ocorreu ! {exc}")   # "exc = excesao"
    conexao.rollback()




# Modo 03
try:
    cursor.execute('INSERT INTO minha_tabela VALUES (?,?)', (1, 'abc'))
    conexao.commit()
except Exception as e:
    print(f"Ops! 'C' Ocorreu um erro ! {e}")
    conexao.rollback()

finally:
    conexao.commit()