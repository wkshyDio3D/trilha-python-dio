
# Retornando Valor com Funcao.

# Usamos "return" para retornar um valor.Por padrao o Python retorna "none" ou seja vazio ou sem valor.
# Em python uma funcao pode retornar mais de um valor.

# Declarando as Funcoes com "return".
def calcular_total(numeros): # Aqui ao ser chamada vai retornar a soma dos numeros.
    return sum(numeros) # Aqui esta retornando "Um" valor.


def retorna_antecessor_e_sucessor(numero): # Aqui ao ser chamada vai retornar os valores antes e depois do "20".
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor # Aqui esta retornando "Dois" valores.

# --- Aqui a baixo temos dois exemplos de retorno "None"- Quando nada e declarado -------------------------
def func_3():
    print("  Ola Mundo! 3 ==>> 'none' ")

def func_4():
    print("  Ola Mundo! 4 ==>> 'none' ")
    return None

# Chamando as Funcoes:
print(calcular_total([10, 20, 34])) # Aqui chamamos a funcao "calcular_total" que vai retornar a soma dos numeros.
 # >>> 64
print(retorna_antecessor_e_sucessor(10))# Aqui chamamos a funcao "retorna_antecessor_e_sucessor" que 
                                        # vai retornar os valores antes e depois do "20". 
  # >>> (9, 11)

print(func_3()) # Aqui como nao foi declarado Nada retorna "none"
print(func_4())