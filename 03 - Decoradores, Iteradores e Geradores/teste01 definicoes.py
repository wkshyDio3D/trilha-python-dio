
# ---  Funcoes de decoracao com Argumantos ---

#

def duplicar(func): # Aqui temos uma funcao de nome "duplicar" que recebe uma funcao =>(func): por argumento.
    def envelope(*args, **kwargs): # Aqui a funcao de "envelope" Recebe  (*args, **kwargs).
        func(*args, **kwargs) # e chama a funcao Duas Vezer passando (*args, **kwargs)
        func(*args, **kwargs) # passando para a (func) que recebeu por referencia.
      

    return envelope # E entao por fim retorna "envelope"

@duplicar # A ser Executado ==> Antes 
def aprender(tecnologia):   # Aqui criamos uma funcao "duplicar" que recebe =>(tecnologia)
    print(f"Estou aprendendo {tecnologia}")   # Aqui ("faz algo antes de executar") 
    print(f"Estou Trabalhando {tecnologia}")  # Aqui ("faz algo Depois de executar") 
    

@duplicar   # A ser Executado ==>Depois 
def trabalho(Mecanica):   # Aqui criamos uma funcao "duplicar" que recebe =>(tecnologia)
    print(f"Estou Trabalhando {Mecanica}")


aprender("mecanica de Aviacao") 

aprender("Python")  # Aqui vai chamar a funcao "aprender" passando atecnologia "python" .



# Podemos usar *args e kwargs na funcao interna , com isso ela aceita um
#  numero Arbitrario de argumentos Posicionais e de Palavras-chave.

