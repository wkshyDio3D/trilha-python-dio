
# Seu código tem boas intenções, mas há um problema importante: você está sobrescrevendo 
# a função incentivar_aprender várias vezes. Em Python (e na maioria das linguagens),
#  quando você declara uma função com o mesmo nome mais de uma vez, somente a última 
# declaração é mantida, e as anteriores são ignoradas.

# Aqui está a explicação:

def incentivar_aprender(nome):
    return f" Oi {nome}, vamos aprender Java juntos!"

def incentivar_aprender(nome):
    return f" Bom_Dia {nome}, vamos aprender HTML juntos!"

def incentivar_aprender(nome):
    return f" Helo {nome}, vamos aprender Python juntos!"
# No trecho acima, apenas a última versão será usada:
# --------------------------------------------------

def incentivar_aprender(nome):
    return f" Helo {nome}, vamos aprender Python juntos!"
# Como resolver isso?
# Você pode criar diferentes funções com nomes distintos, por exemplo:

def incentivar_aprender_java(nome):
    return f"Oi {nome}, vamos aprender Java juntos!"

def incentivar_aprender_html(nome):
    return f"Bom dia {nome}, vamos aprender HTML juntos!"

def incentivar_aprender_python(nome):
    return f"Olá {nome}, vamos aprender Python juntos!"

# Aqui temos o Código corrigido e funcional:

def dizer_oi(nome): 
    return f"Oi {nome}"

def dizer_bom_dia(nome): 
    return f"Bom dia {nome}"

def dizer_helo_whold(nome): 
    return f"Hello {nome}"

def incentivar_aprender_java(nome):
    return f"Oi {nome}, vamos aprender Java juntos!"

def incentivar_aprender_html(nome):
    return f"Bom dia {nome}, vamos aprender HTML juntos!"

def incentivar_aprender_python(nome):
    return f"Hello {nome}, vamos aprender Python juntos!"

def mensagem_para_Washington(funcao_mensagem1):
    return funcao_mensagem1("Washington")

def mensagem_para_guilherme(funcao_mensagem2):
    return funcao_mensagem2("Guilherme")

def mensagem_para_Shaylla(funcao_mensagem3):
    return funcao_mensagem3("Shaylla")

# Chamadas de exemplo:
print(mensagem_para_Washington(dizer_oi))
print(mensagem_para_Washington(incentivar_aprender_java))

print(mensagem_para_guilherme(dizer_bom_dia)) 
print(mensagem_para_guilherme(incentivar_aprender_html))

print(mensagem_para_Shaylla(dizer_helo_whold)) 
print(mensagem_para_Shaylla(incentivar_aprender_python))

# Saída esperada:

# >>> Oi Washington
# >>> Oi Washington, vamos aprender Java juntos!
# >>> Bom dia Guilherme
# >>> Bom dia Guilherme, vamos aprender HTML juntos!
# >>> Hello Shaylla
# >>> Hello Shaylla, vamos aprender Python juntos!