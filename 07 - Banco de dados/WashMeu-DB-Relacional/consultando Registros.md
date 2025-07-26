


# Consulta com unico resultado

 # Usando o Metodo "fetchone()" usado para recuperar um unico registro de resultado. 
 # Retorna o proximo registro na lista ou 'None' se nao houver mais resultados.

# Exemplo de codigo com "fetchone": consultando com um unico resultado.
cursor.execute("SELECT * FROM minha_tabela WHERE id = 1")  # Celecionando apenas o id "1"
cursor.execute("SELECT * FROM minha_tabela WHERE nome = guilherme1")   # Celecionando todos os "guilhermes".
cursor.execute("SELECT * FROM minha_tabela WHERE nome, e-mail = .com")   # Celecionando nomes e e-mail.


cursor.execute("SELECT * FROM minha_tabela WHERE id = 1")
result = cursor.fetchone()
print(result)

# -------------------------------------------------------------------------
# Consulta com todos os resultado:

 # Usando o Metodo "fetchall()" usado para recuperar todos os  registro de resultado. 
 # Retorna uma lista de registros ou uma lista vazia se nao houver mais resultados.

# Exemplo de codigo com "fetchall": consultando todos registros de uma vez.
cursor.execute("SELECT nome FROM minha_tabela") # selecionado todos ==>> "nomes" .
cursor.execute("SELECT e-mail FROM minha_tabela")    # selecionado todos ==>> "e-mail" .
cursor.execute("SELECT nome, e-mail FROM minha_tabela")    # selecionado todos ==>> "nomes e e-mail" .

# Cod:
cursor.execute("SELECT * FROM minha_tabela")    # selecionado todos ==>> "*" .
results = cursor.fetchall()
for row in results:
    print(row)

# ------------------------------------------------------------------------
