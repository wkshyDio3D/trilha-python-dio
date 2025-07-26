

#def dizer_oi(nome): # 01 - Aqui recebe o "nome" apos setr chamado pela primeira => "mensagem_para_guilherme"
 #   return f" Oi {nome}"
    # >>> ' Oi Guilherme'


#def mensagem_para_guilherme(funcao_mensagem):
  #   return funcao_mensagem("Washington")

# mensagem_para_guilherme(dizer_oi) # Aqui chama afuncao (dizer_oi) passando o argumento => "Guilherme" para o "nome".
# mensagem_para_guilherme(incentivar_aprender) # Aqui chama afuncao (incentivar_aprender).

# -----------------------------------------------------------

#def incentivar_aprender(nome):
 #   return f" Oi {nome}, vamos aprender Python juntos!"
    
#def mensagem_para_guilherme(funcao_mensagem):
  #  return funcao_mensagem("Guilherme")

# mensagem_para_guilherme(incentivar_aprender) # Aqui chama afuncao (incentivar_aprender).

# --------------------------------------------------------

def dizer_oi(nome): # 01 - Aqui recebe o "nome" apos setr chamado pela primeira => "mensagem_para_guilherme"
    return f" Oi {nome}"
    # >>> ' Oi Guilherme'

def incentivar_aprender(nome):
    return f" Oi {nome}, vamos aprender Python juntos!"
    # >>> ' Oi Guilherme, vamos aprender Python juntos!'

def mensagem_para_guilherme(funcao_mensagem):
    return funcao_mensagem("Guilherme")

mensagem_para_guilherme(dizer_oi) # Aqui chama afuncao (dizer_oi) passando o argumento => "Guilherme" para o "nome".
                                  # mensagem_para_guilherme(incentivar_aprender) # Aqui chama afuncao (incentivar_aprender).
mensagem_para_guilherme(incentivar_aprender) # Aqui chama afuncao (incentivar_aprender).

