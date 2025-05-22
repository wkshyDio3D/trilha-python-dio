
# Metodos da classe "set" ===>> {pop}

# O "pop" vai removendo os valores da frente "um a um" enquanto
#  voce estiver inserindo 'pop"

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # removendo o (0)
print(numeros.pop())  # Removendo o (1)
print(numeros.pop())  # Removendo o (2)
print(numeros.pop())  # Removendo o (3)
print(numeros.pop())  # Removendo o (4)
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}
