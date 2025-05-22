


# Crie uma Funcao , "elementos_comuns" que receba duas linhas de numeros inteiros separados por espaco:

# def elementos_comuns(tupla):
def elementos_comuns(lista1, lista2):
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    return list(set1.intersection(set2))

# Leitura das listas

lista1 = input().split()
lista2 = input().split()

# Verifique se todos os Elementos da Lista Podem ser Convertidos para Inteiros.
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    

    comuns = elementos_comuns(lista1, lista2)
    print(f" Elementos comuns as duas Listas: {comuns}")
else:
    print("Entrada Invalida")


#  elementos = tuple(map(int, entrada.split()))