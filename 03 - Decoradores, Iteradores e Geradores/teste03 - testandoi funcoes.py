
def dizer_oi(nome): 
    return f" Oi {nome}"

def dizer_bom_dia(nome): 
    return f" bom_dia {nome}"

def dizer_helo_whold(nome): 
    return f" Helo {nome}"
  
# -------------------------------------------

def incentivar_aprender(nome):
    return f" Oi {nome}, vamos aprender Java juntos!"

def incentivar_aprender(nome):
    return f" Bom_Dia {nome}, vamos aprender HTML juntos!"

def incentivar_aprender(nome):
    return f" Helo {nome}, vamos aprender Python juntos!"

# -----------------------------------------------

def mensagem_para_Washington(funcao_mensagem1):
     return funcao_mensagem1("Washington")

def mensagem_para_guilherme(funcao_mensagem2):
    return funcao_mensagem2("Guilherme")

def mensagem_para_Shaylla(funcao_mensagem3):
    return funcao_mensagem3("Shaylla")

mensagem_para_Washington(dizer_oi)
mensagem_para_Washington(incentivar_aprender)

mensagem_para_guilherme(dizer_bom_dia) 
mensagem_para_guilherme(incentivar_aprender)

mensagem_para_Shaylla(dizer_helo_whold) 
mensagem_para_Shaylla(incentivar_aprender) 





