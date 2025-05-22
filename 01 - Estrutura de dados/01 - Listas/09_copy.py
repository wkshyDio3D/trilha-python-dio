
# ================   COMANDO [] COPY   ===========================

# A lista e um objeto Mutavel. Se eu passo ela para outro DEV usar em outra parte do Codigo.
#  Tudo que eu modificar na minha lista vaise refletir na lista original que esta sendo usada pelo outro DEV. 
# Para evitar que isso ocorra eu uso o comando COPY. 

# O copy Vai retornar Uma Lista Identica Porem com uma instacia Diferente ou seja nao e a mesma lista . 
# Agora tudo que eu modificar na minha lista nao vai interferir na lista original que esta sendo utilizada pelo outro DEV.

# Aqui Temos a lista Original ===>>> lista = [1, "Python", [40, 30, 20]]  <<<===

# lista = [1, "Python", [40, 30, 20]]

# lista.copy()

# print(lista)  # [1, "Python", [40, 30, 20]]

# Saida >>> [1, "Python", [40, 30, 20]]

# -----------------------------------------------------------

# Aqui Temos a lista Original e a lista copiada como ===>> L2

lista_1 = [1, "Python", [40, 30, 20]]

l2 = lista_1.copy()

print("Saida > lista_1 >>> ", lista_1)  # Saida >>> [1, "Python", [40, 30, 20]]
print("Saida >    L2   >>> ", l2)     # Saida >>> [1, "Python", [40, 30, 20]]

print(id(l2), id(lista_1))
# Aqui prova que as lista sao de diferente estancias, pois tem o id diferente.
#  de forma que uma nao interfere na outra.

print ("id ===>>> ", id(l2),"   id ===>>> ",  id(lista_1))


# Aqui os iten foran auterados na lista "L2" mais nao foram auterados na "lista_1"
l2[1] = "wash"                  # L2 na posicao "1" = "wash"
l2[0] = 50                      # L2 na posicao "0" = 50
l2[2] = [100, 75, 50, 25, 0]    # l2 na posicao "2" ==>> [100, 75, 50, 25, 0]

print(lista_1)
print(l2)
