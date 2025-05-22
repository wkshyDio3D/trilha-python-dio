
# --- Acessando dados para Extrair conjunto de valores de uma sequencia. --

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]    # iniciando a partir da posicao 2 ate o final.
print(lista[:2])  # ["p", "y"]              # iniciando a partir da posicao 0 ate a posicao 2 ==> 2-1.
print(lista[1:3])  # ["y", "t"]             # iniciando a partir da posicao 1 ate a posicao 3.
print(lista[0:3:2])  # ["p", "t"]           # iniciando a partir da posicao 0 ate a posicao 3. e o STep 2.
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]  # Nao passando as posicoe inicial, final, e nem o step.
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]    # Espelhando a sequencia colocando -1 no final.


# NO Fatiamento podemos Extrair conjunto de valores de uma sequencia. 
# Para isso basta passar o INDICE inicial e/ou FINAL para acessar o conjunto.
#  podemos ainda informar quantas posicoes o cursor deve"PULAR" no acesso. 