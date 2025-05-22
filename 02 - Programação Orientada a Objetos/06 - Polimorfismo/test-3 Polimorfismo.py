

class Passaro:
    def voar(self):
        print("Quem Esta Voando ...\t")

class Pardal_01(Passaro):
    def voar(self):
        print(" Pardal-01 Voando...")
        # return super().voar()

class Pardal_02(Passaro):
    def voar(self):
        print(" Pardal-02 Voando...")
        # return super().voar()

class Avestruz(Passaro):
    def voar(self):
        print(" Avestrus Nao Pode Voar...")
        # return super().voar()

# FIXME: Exemplo Ruim do uso de "Hernaca" para "ganhar" o metodo "voar".
class Aviao(Passaro):
    def voar(self):
        print(" Aviao Decolando...")
        # return super().voar()

def Plano_de_voo(obj):
    obj.voar()

# Aqui estamos Passando a Instancia para as variaveis p1,p2,p3 e p4.
Plano_de_voo(Passaro())
print("")

p1 = Pardal_01()
p2 = Pardal_02()
p3 = Avestruz()
p4 = Aviao()

Plano_de_voo(p1)
Plano_de_voo(p2)
Plano_de_voo(p3)
Plano_de_voo(p4)

print("")
# Aqui estamos Passando as Instancias diretamente para o Plano de Voo.
Plano_de_voo(Passaro())
print("")

Plano_de_voo(Pardal_01())
Plano_de_voo(Pardal_02())
Plano_de_voo(Avestruz())
Plano_de_voo(Aviao())