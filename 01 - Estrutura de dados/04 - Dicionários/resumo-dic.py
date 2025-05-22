

# declarando Dicionario. 
print(" # declarando Dicionario. ")
pessoa = {"nome": "Guilherme", "idade": 28} 
print(pessoa)
pessoa = dict(nome="Guilherme", idade=28) 
print(pessoa)
pessoa["telefone"] = "3333-1234"  
print(pessoa)
print("------------------------------------")

print ("aqui Estamos Acessando dados.")
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"
print("Antes : ", dados)
print("------------------------------------")

print(" # Aqui Estamos auterando valor.")
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"
print("Depois : ", dados)  
print("------------------------------------")

print(" # Aqui Estamos Deletando Contato/s.")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]


# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)


print(contatos)

print("------------------------------------")
