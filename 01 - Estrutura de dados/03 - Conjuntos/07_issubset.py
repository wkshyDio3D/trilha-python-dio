
# Metodos da classe "set" ===>> {issubset} .

conjunto_a = {1, 2, 3}              # Elementos de "a"
conjunto_b = {4, 1, 2, 5, 6, 3}     # Elementos de "b"

resultado = conjunto_a.issubset(conjunto_b)  # True
# Aqui os elementos de "a" estao em "b". - E "verdadeiro"
print(resultado)
# >>> True


resultado = conjunto_b.issubset(conjunto_a)  # False
# Aqui os elementos de "b" nao estao em "a". - E "Falso"
print(resultado)
# >>> False