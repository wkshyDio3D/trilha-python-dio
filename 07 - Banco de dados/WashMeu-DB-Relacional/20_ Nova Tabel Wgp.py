
# Cadastro de Clientes com Detecção de Colunas e Menu

import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
db_path = ROOT_PATH / "Cadastro de Clientes_wgp.sqlite"

conexao = sqlite3.connect(db_path)
cursor = conexao.cursor()

# Criar tabela básica (sem telefone e funcao ainda)
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    email VARCHAR(150)
)
""")
conexao.commit()

# Verifica colunas existentes
cursor.execute("PRAGMA table_info(clientes)")
colunas = [coluna[1] for coluna in cursor.fetchall()]

# Adiciona coluna telefone se não existir
if "telefone" not in colunas:
    cursor.execute("ALTER TABLE clientes ADD COLUMN telefone VARCHAR(20)")
    print("🛠️ Adicionada coluna 'telefone'.")

# Adiciona coluna funcao se não existir
if "funcao" not in colunas:
    cursor.execute("ALTER TABLE clientes ADD COLUMN funcao VARCHAR(50)")
    print("🛠️ Adicionada coluna 'funcao'.")

conexao.commit()

# Funções CRUD com os novos campos
def inserir_cliente():
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    funcao = input("Função: ")
    cursor.execute("INSERT INTO clientes (nome, email, telefone, funcao) VALUES (?, ?, ?, ?)",
                   (nome, email, telefone, funcao))
    conexao.commit()
    print("✅ Cliente cadastrado com sucesso!\n")

def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    if not clientes:
        print("Nenhum cliente encontrado.\n")
    else:
        print("📋 Lista de Clientes:")
        for cliente in clientes:
            print(f"ID: {cliente[0]} | Nome: {cliente[1]} | E-mail: {cliente[2]} | Telefone: {cliente[3]} | Função: {cliente[4]}")
        print()

def atualizar_cliente():
    id = input("ID do cliente: ")
    novo_nome = input("Novo nome: ")
    novo_email = input("Novo e-mail: ")
    novo_telefone = input("Novo telefone: ")
    nova_funcao = input("Nova função: ")
    cursor.execute("UPDATE clientes SET nome = ?, email = ?, telefone = ?, funcao = ? WHERE id = ?",
                   (novo_nome, novo_email, novo_telefone, nova_funcao, id))
    conexao.commit()
    print("🔄 Cliente atualizado com sucesso!\n")

def deletar_cliente():
    id = input("ID do cliente para deletar: ")
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conexao.commit()
    print("❌ Cliente removido com sucesso!\n")

def menu():
    while True:
        print("=== MENU CLIENTES ===")
        print("[1] Cadastrar cliente")
        print("[2] Listar clientes")
        print("[3] Atualizar cliente")
        print("[4] Remover cliente")
        print("[0] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            atualizar_cliente()
        elif opcao == "4":
            deletar_cliente()
        elif opcao == "0":
            print("👋 Encerrando...")
            break
        else:
            print("❗ Opção inválida. Tente novamente.\n")

    conexao.close()

if __name__ == "__main__":
    menu()
