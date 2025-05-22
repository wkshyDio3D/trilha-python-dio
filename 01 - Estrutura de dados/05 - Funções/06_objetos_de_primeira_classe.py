
# ----- Objetos de Primeira Classe.
# Uma Funcao e um Objeto de Primeira classe . Podemos atribuir "funcoes a Variaveis", 
# Passa-las como Parametros para Funcoes, e usa-las como valor em estruturas de 
# dados (Lista, Tuplas, Dicionarios, etc) e usalas como valor de retorno par uma funcao(closures).

def somar(a, b):    # Primeira funcao de Somar Dois argumento a e b
    return a + b    # Aqui retorna a + b

def subtrair(a, b):    # Primeira funcao de Subtrair Dois argumento a e b
    return a - b    # Aqui retorna a - b

def multiplicar(a, b):    # Primeira funcao de Somar Dois argumento a e b
    return a * b    # Aqui retorna a * b

def dividir(a, b):    # Primeira funcao de Somar Dois argumento a e b
    return a / b    # Aqui retorna a / b

def test_1(a, b):
    return a * 2 + b * 3

def test_1(a, b):
    return a * 2 + b * 3

# -------------------------------------------------------
def exibir_resultado(a, b, funcao): #segunda funcao 
    resultado = funcao(a, b)
    # print(f"  Resultado da operação {a} + {b} = {resultado}")
    print(f"  Resultado da operação e ==>> {resultado}")
    #vprint(resultado)
# ------------------------------------------------------------
exibir_resultado(10, 5, somar)  # O resultado da operação 10 + 5 = 15

exibir_resultado(10, 5, subtrair)  # O resultado da operação 10 - 5 = 5

exibir_resultado(10, 5, multiplicar)  # O resultado da operação 10 * 5 = 50

exibir_resultado(10, 5, dividir)  # O resultado da operação 10 / 5 = 2.0

exibir_resultado(10, 5, test_1)  # O resultado da operação 10 * 2 + 5 * 3 = 35



op = somar

print(op(1, 23))