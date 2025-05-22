
# ------ Acessando os Dados de um SET -------

# Conjuntos em python "nao suportam indexacao e nem fatiamento",
#  caso queira acessar os seusvalores ou itens e necessario 
# converter o conjunto para "LISTA".

# Exemplo 1
numeros = {1, 2, 3, 2}  # Conjunto {Sets} ==>> para assesar o valor do index "0"
numeros = list(numeros) # aqui convertemos o conjunto set {numeros}
                        # para (list).
print(numeros[0])       # Agora podemos acessar o valor do index "0" que e "1"

print(" ")

# Exemplo 2
numeros = {1, 2, 3, 2}  
numeros = list(numeros) 
print(numeros[2])       # Agora podemos acessar o valor do index "2" que e "3"


# Exemplo 3
# Se tentar  acessar direto vai dar erro.
numeros = {1, 2, 3, 2}  
print(numeros[0])       # 
numeros = list(numeros) 

# TypeError: 'set' object is not subscriptable