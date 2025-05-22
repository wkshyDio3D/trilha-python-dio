

# Programacao Construtores e Derstruidores -------------
# Etapa 1
# Conhecendo Os Metodos "__init__" e "__del__" .
# O metodo Construtor ou "__init__" ou Inicializador, e executado quando uma nova class 
# ou  Instacia e criada, e inicializando o estado do nosso Objeto. 
# Para Declarar o Metodo construtor da "class", criamos um Metodo com o nome __init__.
 
# __init__

class Cachorro:     # aqui temos a Classe.
    def __init__(self, nome, cor, acordado=True): # def - vai receber - > nome, cor e acordado.
        print(" Inicializando a Class...Cachorro ")
        self.nome = nome     # Aqui temos os Atributos e as caracteristica da nossa class.
        self.cor = cor
        self.acordado = acordado
        # pass

    def __del__(self):
        print(" Removendo a instacia da Classe. ")

    def latir(self):
        print(" Inicializando o Metodo Latir ")
        print( " auau ")

def criar_novo_cachorro():
    c = Cachorro(" Zeus ", " Branco e Preto", False )
    print(c.nome)        

c = Cachorro(" Chappie ", " Amarelo ")  # ==>> Aqui => Inicializando a Class..."Cachorro".

c.latir()   # ==>> Aqui => Inicializando o Metodo "Latir".

criar_novo_cachorro() # ==> Aqui => Chama o metodo "criar_novo_cachorro".

print(" Ola Mundo_1 ")
print(" Ola Mundo_2 ")

# Forcando o uso do del.
del c
print(" Ola Mundo_3 ")
print(" Ola Mundo_4 ")
print(" Ola Mundo_5 ")

# __del__  O "__del__" Nao e Muito Utilizado poeque o python ja se encarega de limpar a instacia da memoria .
# 
# class Cachorro:
    # def __del__(self):
    #     print(" Removendo a instacia da Classe. ") 
# c = Cachorro()
# del c