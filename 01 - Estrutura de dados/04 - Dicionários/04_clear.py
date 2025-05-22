
# ---------------- Metodo {}.Clear.py -----------------

# O Metodo clear Simplesmente  apaga ou deleta todo o conteudo do Dicionario.

# Tenha certeza ao utilizar o metodo Clear.

# Aqui Estamos Criando todos os contatos da nossa Biblioteca.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

print("Contatos Criados ==>>> ",contatos) # Aqui mostra os contatos Criados 

contatos.clear() # # Aqui Estamos Apagando ou Deletando todos os contatos da nossa Biblioteca.
print(contatos)  # {} # Aqui Mostra que Nao existem Mais contatos.
print("Contatos Deletados ==>>> ", contatos) 