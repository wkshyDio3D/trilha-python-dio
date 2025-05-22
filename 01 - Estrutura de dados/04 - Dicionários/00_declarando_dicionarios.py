
# -------- Dicionario -----------------

#       Objetivo =>> Entender o funcionamento , estrutura de Dados, Como Declarar,
# Apagar Valores, Adcionario e etc.
#       Dicionario e um conjunto nao_ordenado de pares "Chave:Valor",
#  Onde as Chaveis sao Unicas . O dicionario sao delimitados por "chave: {},
#  e contem uma lista de Pares separada por Virgula.
# As "Chaves" devem ser um objeto imutavel ===> Exe. tupla ou string.
# Os "Valores" Pode, ser Qualquer Tipo de Objeto.
# Para declarar Um Dicionario Utiliza-se Chave ==>>> "{}" ou ==>>> "Dict" Que e a classe Do Python.
# Exemplo Dicionario =>> "pessoa" ==> onde a chave ===>> "nome" e o valor ===>> "Guilherme".
#                        "pessoa" ==> onde a chave ===>> "idade" e o valor ===>> "28".

pessoa = {"nome": "Guilherme", "idade": 28} # Aqui Usamos a chave {} Para adicionar os valores {"Chave":"Valor"}.
print(pessoa)
# >>> {'nome': 'Guilherme', 'idade': 28}

pessoa = dict(nome="Guilherme", idade=28) # Aqui Usamos o"dict" Para adicionar os valores ==>> dict(Chave = "Valor").
                                          # Entre parentese(Onde sao passados os dois valores).
print(pessoa)
# >>> {'nome': 'Guilherme', 'idade': 28}

pessoa["telefone"] = "3333-1234"  # Aqui Quando Ja tem um dicionario criado e estamos adcionando uma 
                                  # nova Chave no dicionario. Estamos adcionando 
                                  # a chave ==>> "telefone" e o objeto ==>> "3333-1234".
print(pessoa)
# >>> {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

pessoa["nome"] = "Maria" # Aqui estamos sobrescrevendo ou substituindo "Guilherme " por "Maria"
print(pessoa)
# >>> {'nome': 'Maria', 'idade': 28, 'telefone': '3333-1234'}