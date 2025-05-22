
# Metodos da classe "set" ===>> {difference} ou diferente.

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
# Vai pegar apenas no conjunto "a =>{1}" e nao estiver no conjunto "b => {2, 3, 4}".
print(resultado)
# >>> {1}



resultado = conjunto_b.difference(conjunto_a)
# Vai pegar apenas no conjunto "b =>{4}" e nao estiver no conjunto "a => {1, 2, 3}".
print(resultado)
# >>> {4}