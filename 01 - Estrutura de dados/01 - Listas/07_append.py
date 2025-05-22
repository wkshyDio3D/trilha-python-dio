
# ================   Comando [] "Append".   =======================

# Usado para adicionar um novo elemento a minha lista ja criada. 

lista = []

lista.append(1)                 # Aqui adiciona o Objeto ==>> 1.
lista.append("Python")          # Aqui adiciona o Objeto tipo String ===>>> 'Python'.
lista.append([40, 30, 20])      # Aqui adiciona o Objeto tipo Lista ===>>>'40, 30, 20'.

print(lista)  # [1, "Python", [40, 30, 20]]  # Aqui temos a lista com os objetos adicionados.
# >>> [1, 'Python', [40, 30, 20]]


# Aqui nessa Lista Temos o Objeto   "1"           na posicao '0', 
#                        o objeto "Python"        na posisao '1',
#                o objeto lista "[40, 30, 20]"    na posicao '2'.

lista.append("Wash")          # Inserindo + 1 Objeto a lista

print(lista)
# >>> [1, 'Python', [40, 30, 20], 'Wash']