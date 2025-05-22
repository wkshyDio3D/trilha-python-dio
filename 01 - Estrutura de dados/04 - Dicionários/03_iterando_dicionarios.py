
# Interando ou interagindo com Dicionarios - Aninhados .

# acessando Valores do nosso Dicionario. Utilizando o Nome do nosso dicionario 
# Principal ==>> "contatos" e a o nome de um sub-dicionario.

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Aqui temos duas formas de acessar o nosso dicionario. 

# primeira forma . Funciona mais nao e a melhor forma.
for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

# segunda Forma. E a melhor forma e inclui a funcao "Items"
for chave, valor in contatos.items():
    print(chave, valor)
