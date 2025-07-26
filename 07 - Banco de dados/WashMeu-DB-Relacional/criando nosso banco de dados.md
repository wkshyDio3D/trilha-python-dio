O erro está nesta linha do seu código:

python
Copiar
Editar
cursor = exec("CREATE TABLE clientes (...)")
🔍 Problema:
Você usou a função exec(), que é uma função Python para executar código Python (e não comandos SQL). Como "CREATE TABLE ..." é um comando SQL, o Python tenta interpretá-lo como código Python, e isso causa o erro de SyntaxError.

✅ Correção:
Para executar comandos SQL com sqlite3, você deve usar o método .execute() do cursor.

✔ Código corrigido:
python
Copiar
Editar
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_washbanco.sqlite")    
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")

conexao.commit()  # importante para salvar as alterações no banco
conexao.close()
🔒 Notas importantes:
Use CREATE TABLE IF NOT EXISTS para evitar erro se a tabela já existir.

Sempre chame conexao.commit() após alterações no banco.

Lembre-se de fechar a conexão com conexao.close().