
# Conhecendo Tuplas em python 
# 
# A Irma da lista - Entender o funcionamento e a estrutura de dados tuplas.
# Metodos e onde se utiliza a tupla. 
# Difernte da lista que e Mutavel a tupla e "imutavel" . Ou seja seus valores
#  nao podem ser auterados depois de criados .
# 
# Podemos criar tuplas atraveis da classe TUPLE, ou colocando valores separados
#  por virgulas de parenteses.
# Declarando Tuplas ou Criando Tuplas

frutas = ("laranja","pera","uva",) # Aqui entre parenteses se coloca uma virgula no final, 
                                   # indicando para o python que se trata de uma TUPLA e 
                                   # nao de uma LISTA.ok 
print(frutas) 
# >>> ('laranja', 'pera', 'uva')

letras = tuple("python")
print(letras)
# >>> ('p', 'y', 't', 'h', 'o', 'n')

numeros = tuple([1, 2, 3, 4])
print(numeros)
# >>> (1, 2, 3, 4)

pais = ("Brasil",)
print(pais)
# >>> ('Brasil',)