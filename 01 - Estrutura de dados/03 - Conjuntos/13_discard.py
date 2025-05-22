
# Metodos da classe "set" ===>> {discard}
# No metodo "set" nao aceita valores duplicados. se voce inserir
#  valores duplicado eles serao descartados.

numeros = {1, 2, 3, 1, 2, 4, 0, 5, 5, 6, 7, 8, 9, 2, 8, 0}
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1) # Descartando o valor (1).
print(numeros)

numeros.discard(45) # Descartando o valor (45). Como o (45) nao
                    # existe nao vai dar erro e prosegue normalmente.
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
