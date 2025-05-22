
# Programacao Construtores e Derstruidores -------------

# 

class Cachorro:  # Aqui Temos a Classe Cachorro.
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def latir(self):
        print("Auau")

    def falar(self):
        print("Oiiiii")

    def dormir(self):
        self.acordado = False
        print("Zzzzz...")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()
c.latir()

print("Ola mundo")

del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()

#  ------ Criando o Objeto --------------


cao_1 = Cachorro("Mimi", "Marron") # Aqui esta acordado.

print(cao_1.acordado)
cao_1.dormir()
print(cao_1.acordado)


cao_2 = Cachorro("Aladim", "Branco e Preto") # Aqui esta acordado.

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)