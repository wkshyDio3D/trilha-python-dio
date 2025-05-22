
# Metodos da classe "set" ===>> {isdisjoint} ou {disjunto} diferente de {union} os conjuntos nao se tocao estao separados.

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
# Aqui os elementos de "b" nao estao em "a". - # "True"
print(resultado)
# >>> True

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
# Aqui os elementos de "c" nao estao em "a". - # "Falso"
print(resultado)
# >>> False