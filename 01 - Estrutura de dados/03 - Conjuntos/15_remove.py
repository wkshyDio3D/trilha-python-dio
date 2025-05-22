
# Metodos da classe "set" ===>> {remove}
# No metodo "Remove" se voce tentar remover um valor que nao 
# existe vai dar erro e nao prosegue normalmente.

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}


numeros.remove(45) # Descartando o valor (45). Como o (45) nao
                    # existe vai dar erro e nao prosegue normalmente.
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}