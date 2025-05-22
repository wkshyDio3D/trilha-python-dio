
# ------- Teste DIO Tuple Aprovado ---------------

# No "TODO" , abaixo: Crie a funcao 'soma_tupla' para receber
#  uma tupla de numeros inteiros como argumentos:

print(" Mytupla 1")
print(" Entre com 2 valores separados por espaco para somar ok")

def soma_tupla(tupla):
    return sum (tupla)
    

if __name__ == "__main__":
    entrada = input()

# No "TODO" , abaixo: Defina tupla para receber os numeros inteiros:
    elementos = tuple(map(int, entrada.split())) # Aqui o nome correto e "tuple" nao tupla.
   
    resultado = soma_tupla(elementos)
    print(f" A Soma dos elementos da Mytupla_1 e: {resultado}")

 # (map(int, entrada.split())) ==>> trasforma aentrada em uma sequencia de Inteiros.
    # Tuple(...) ==>>  Converte a sequencia em uma tupla, como pedido.
    # A funsao "def soma_tupla(tupla):" Calcula e retorna a soma de todos os elementos.

# ------- Brincando com Tuplas ---------------
print(" Mytupla 2")
def mytupla():
    tupla = (1, 2, 3)
    print(tupla)

mytupla()