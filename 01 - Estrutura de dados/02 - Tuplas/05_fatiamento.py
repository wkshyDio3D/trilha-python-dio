
# -------- Fatiamento de tuplas --------------

# indice  0 -  1 -  2 -  3 -  4 -  5 
tupla = ("p", "y", "t", "h", "o", "n",)

# Para isso pasamos o indice INICIAL - FINAL - e o -STEP.

print(tupla[2:])  # ("t", "h", "o", "n")  ==>> Aqui usamos apenas o indice inicial "2".
print(tupla[:2])  # ("p", "y")            ==>> Aqui usamos apenas o indice final "2".
print(tupla[1:3])  # ("y", "t")           ==>> Aqui usamos o indice inicial "1" e o final "3".
print(tupla[0:3:2])  # ("p", "t")       ==>> Aqui usamos o indice inicial "0" final "3" eo step "2".
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")      ==>> Aqui usamos apenas o "::"
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")    ==>> Aqui usamos apenas o "::-1" para inverter

# Podemos extrair um conjunto de valores de uma sequencia. Usando o
#  indice INICIAL e/ou final para acessar o conjunto. E ainda podemos
#  informar quantas posicoes o cursor deve "pular" no acesso.


# Interando usndo FOR
for tup in tupla:
    print(tup)

for indice, tup in enumerate(tupla):
    print(f"{indice}: {tup}")