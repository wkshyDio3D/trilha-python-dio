
# ----------- Sets --------------

# Um "sets" e uma colecao que nao possui objetos repetidos,
#  usado para representar conjuntos Matematicos ou eliminar 
# itens duplicados de um interavel.

numeros = set([1, 2, 3, 1, 3, 4])                # Eliminado Numeros duplicados.
print(numeros)  
# >>> {1, 2, 3, 4}

letras = set("abacaxi")                          # Eliminado Letras duplicadas.
print(letras)  
# >>> {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio")) # Eliminado Objetos duplicados.
print(carros)  
# >>>  {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"}       # Eliminado itens duplicados.

print(linguagens)
# >>> {'java', 'python'}

