


class Passaro:
    def voar(self): # pass
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj):
    obj.voar()

# plano_voo(Passaro())  # chamando o 'Metodo' -> (Passaro())

plano_voo(Pardal())     # chamando o 'Metodo' -> (pardal())
plano_voo(Avestruz())   # chamando o 'Metodo' -> (Avestruz())
plano_voo(Aviao())      # chamando o 'Metodo' -> (Aviao())
