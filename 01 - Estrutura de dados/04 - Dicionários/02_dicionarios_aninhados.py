
# Dicionarios Aninhados 

# Sao semelhantes ao utilizados em bancos de dados "bd".

# Dicionarios podem armazenar qualquer tipode objeto python como Valor, 
# desde que a chave para esse valor seja umobjeto imutavel 
# como (String ou Numeros).

# Aqui no nosso Exemplo estamos utilizando uma string de "@mail" 
# ou poderia ser outra (String ou Numeros).
print("------------- Contato  conm Dicionarios Aninhados -------------")
# Exemplo1 ==>> Aqui estamos criando um dicionario 
# ("contatos" com uma chave de (String ou Numeros)"guilherme@gmail.com":)), 
# e pra cada um dicionario adicionamos um Novo Dicionario com {"chave": "valor"},
# exemplo 1 ==>> "2025":{"chave_1": "valores_1", "chave_...": "valores_...", "chave_fim": "valores_fim"},  
# exemplo 2 ==>> "dvile@mail.com":{"chave_1": "valores_1", "chave_...": "valores_...", "chave_fim": "valores_fim"}, 

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},  # primeiro Dicionario.
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},    # segundo  Dicionario.
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871", "extra": {"a": 1}}, # Terceiro Dicionario. Aqui adicionamos mais 1 item "Extra" ao nosso dicionario.
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

extra = contatos["chappie@gmail.com"]["extra"]["a"]     # Aqui acessando o item "extra" do dicionario ==>>["chappie@gmail.com"].
print("extra", extra)
# >>> 1

# Acessando contatos.
# Para acessar o "telefone", do  contato "Melaine", Basta adicionar entre couchetes a primeira chave ==>> ["melaine@gmail.com"],
#  e a segunda chave ["telefone"] 
# 
telefone = contatos["melaine@gmail.com"]["telefone"]  
print(telefone)
# >>> # "3443-2121"

# Para acessar o "nome", do contato "Melaine", Basta adicionar entre couchetes a primeira chave ==>> ["melaine@gmail.com"],
#  e a segunda chave ["nome"] 
# 
telefone = contatos["melaine@gmail.com"]["nome"]  
print(telefone)
# >>> # "Melaine"

# Para acessar o "Todos os detalhes ", do contato "Melaine", Basta adicionar entre couchetes a primeira chave ==>> ["melaine@gmail.com"],

telefone = contatos["giovanna@gmail.com"]  
print(telefone)
# >>> {'nome': 'Giovanna', 'telefone': '3443-2121'}

print(contatos) # Aqui mostra Todos os Contados da biblioteca.

print("------------- Contato Agenda --com Dicionarios Aninhados -------------")

agenda = {
    "2025": {"nome": "Guilherme", "telefone": "3333-2221"},
    "sheryDvile": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "ano2015": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = agenda["ano2015"]["telefone"]  
print(telefone)
# >>> 

telefone = agenda["2025"]["telefone"]  
print(telefone)
# >>> 

telefone = agenda["chappie@gmail.com"]  
print(telefone)
# >>> 

print(contatos) # Aqui mostra Todos os Contados da biblioteca.