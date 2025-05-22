
# ------- Compreensao de lista -----------------

# Filtrar lista
# Filtrando todos os numeros pares de uma lista fornecida. 
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
# Exemplo Elevando todos os numeros ao quadrado
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
