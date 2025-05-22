


def exibir_mensagem():  # Nome dessa Funcao ==>> exibir_mensagem():
    print("    Menu! Olá mundo!")
    # Aqui Retorna ==>> ("Menu! Olá mundo!")

def exibir_mensagem_2(submenu_2):
    print(f"Menu 2 =>> {submenu_2}!\n")
    # Menu 2 =>> submenu_2!

def exibir_mensagem_3(submenu_3="Anônimo"):
    print(f"Menu 3 =>>> {submenu_3}!\n")
    # >>> Menu 3 =>>> Anônimo!
    # >>> Menu 3 =>>> submenu_3!

exibir_mensagem() # Aqui Retorna ==>> ("Menu! Olá mundo!")
exibir_mensagem_2(submenu_2="submenu_2") 
exibir_mensagem_3() # Aqui Retorna ==>> "Anônimo")
exibir_mensagem_3(submenu_3="submenu_3")

# ttggg   


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

# -------------------------------------------------
# ------------ Somando Dois Numeros ---------------
def somar(a, b):    # Primeira funcao de Somar Dois argumento a e b
    return a + b    # Aqui retorna a + b
# -------------------------------------------------------
def exibir_resultado(a, b, funcao): #segunda funcao 
    resultado = funcao(a, b)
    print(f"  Resultado da operação {a} + {b} = {resultado}")
    print(f"  Resultado da operação e ==>> {resultado}")
    print(resultado)
# ------------------------------------------------------------
exibir_resultado(10, 5, somar)  # O resultado da operação 10 + 5 = 15

