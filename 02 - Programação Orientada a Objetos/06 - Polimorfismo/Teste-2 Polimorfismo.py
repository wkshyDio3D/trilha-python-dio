

class Passaro:
    def voar(self):
        print(" Voando ... ")

class Pardal(Passaro):
    def voar(self):
        print("Pardal 01 Voando")

class Pardal_02(Passaro):
    def voar(self):
        print("Pardal 02 Voando")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

def Quem_esta_Voando(obj):
    obj.voar()



# Chamando a classe

Quem_esta_Voando(Pardal())

Quem_esta_Voando(Pardal_02())

Quem_esta_Voando(Avestruz())

