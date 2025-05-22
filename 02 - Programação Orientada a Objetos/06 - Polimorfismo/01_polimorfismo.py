
# ---- Polimorfismo -----------

# No Heranca a 'Classe Filha' herda os 'metodos' do da 'Classe pai' .
# Porem e Possivem Modificar um 'Metodo'em uma 'Classe Filha' herdada 
# da 'Classe Pai'. E Isso Eutil nos casos que o 'Metodo' herdado
#  da 'classe pai' nao se encaixa perfeitamente na 'Classe filha'
# Exemplo: Na (classe Pai     -> os Passaros Voam).
#          Na (classe filha 1 -> o Pardal voa ).
#          na (Classe filha 2 -> Avestruz nao voa).

class Passaro:
    def voar(self):
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


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
