
# ----- Interar Lista ou Percorrendo os dados de uma Lista. ---------

# A forma mais comum para percorrer os dados de uma lista e utilizando "FOR".

carros = ["gol", "celta", "palio"]

for carro in carros:    # Aqui Vai percorrer toda a lista
    print(carro)        # Aqui Vai Exibir toda a lista

# >>> gol
# >>> celta
# >>> palio

print(" ")

#-------------- Usando a Funcao Enumerate. --------------------
# AS vezes e necesario saber qual o indice do objeto dentro do laco "For".
#  Para isso usamos a funcao "Enumerate".  

# Onde Temos o contador"indice", o item da iteracao"carro e coloca o interavel dentro da funcao "enumerate(carros)".
for indice, carro in enumerate(carros): 
    print(f"{indice}: {carro}")

# >>> 0: gol
# >>> 1: celta
# >>> 2: palio