
# Metodos da classe "set" ===>> {symmetric_difference} ou diferente simeticamente.
# Difererte do intercection ==> esse Vai peger tudo que estiver Fora da Itersection.

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
# Vai pegar apenas o que estiver Fora da Itersection "a =>{1}" e no conjunto "b => {4}".

print(resultado)
# >>> {1, 4}