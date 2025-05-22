
# Metodos da classe "set" ===>> {issuperset} . contrario do {issubset}

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
# Aqui os elementos de "b" nao estao em "a". - E "Falso"
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
# Aqui os elementos de "a" nao estao em "b". - E "True"
print(resultado)
