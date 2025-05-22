
# --------- Escopo Local e Escopo Global ---------------

# Dentro do Bloco da Funcao "def" o Escopo e local. Onde alteracoes ali feita em objetos  
# imutaveis serao perdidas quando o metodo terminar de ser executado.
# Para usar objetos Globais utilizamos a Palavra-chave "global", que informa ao interpretador
#  que a variavel que esta sendo manipol;ada no escopo local e global.
# essa nao e uma boa pratica  e deve ser Evitada.

# Devese evitar de utilizar escopo global

salario = 2000  # Variavel de Escopo global fora do Bloco de funcao "def".

def salario_bonus(bonus):
    global salario

    lista_aux = lista.copy()    # Aqui fazemos uma copia da lista [1]
    lista_aux.append(2)
    print(f" Lista Auxiliar = {lista_aux}") # Aqui temos o resultyado da lista [2] 
                                            # sem interferir na lista [1].

    salario += bonus
    return salario


# salario_bonus(500)  

lista = [1]

salario_com_bonus = salario_bonus(500)   # 2500
print(salario_com_bonus)

print(lista)