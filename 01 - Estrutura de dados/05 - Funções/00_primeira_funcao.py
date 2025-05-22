
# ---------- Funcoes ----------------

# "Funcao" e um bloco de codigo identificado por um "Nome", e pode receber uma 'lista' de "Parametros", 
# que pode "Ter" ou "Nao"  Valores "Padroes". 
# A "Funcao" Torna o codigo Mais Legivel e possibilita o Reaproveitamento de "Codigo". 
# "Funcao" e o mesmo que Programar de Maneira Estruturada.

# "def" ==>> Informa ao Interpretador que estamos trabalhando com uma "Funcao".

# Aqui Estamos Declarando as funcoes.. Que so Vao funcionar se for chamadas.
def exibir_mensagem():  # Nome dessa Funcao ==>> exibir_mensagem():
    print("  1 ==>> Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="  3 ==>> Anônimo"):
    print(f"Seja bem vindo {nome}!")

# Aqui Estamos Chamando as Funcoes.. Para ser Executada.
exibir_mensagem() # ("Olá mundo!")
exibir_mensagem_2(nome="  2 ==>> wash")
exibir_mensagem_3() # Aqui , como nao foi passado nenhum valor, vai "retornar" ==>> "  3 ==>> Anônimo"
exibir_mensagem_3(nome="  4 ==>> Chappie")

exibir_mensagem_3() # Aqui , como nao foi passado nenhum valor, vai "retornar" ==>> "  3 ==>> Anônimo"
exibir_mensagem_3(nome="  5 ==>> WEp")

exibir_mensagem() # ("Olá mundo!")
exibir_mensagem_2(nome="  6 ==>> Guilherme")

exibir_mensagem_2(nome="  7 ==>> Wilborn")
exibir_mensagem_3() # Aqui , como nao foi passado nenhum valor, vai "retornar" ==>> "  3 ==>> Anônimo"
exibir_mensagem_3(nome="  8 ==>> Chappie")


exibir_mensagem() # ("Olá mundo!")
exibir_mensagem_3() # Aqui , como nao foi passado nenhum valor, vai "retornar" ==>> "  3 ==>> Anônimo"
exibir_mensagem_3(nome="  9 ==>> WepStore")

exibir_mensagem() # ("Olá mundo!")
exibir_mensagem_2(nome=" 10 ==>> Makayla")
