

class Veiculo: # Aqui a "classe Veiculo" e a classe "Mae"
    def __init__(self, marca, modelo, cor, placa, rodas):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.rodas = rodas
        # pass

    # Agora Vamos definir os comportamentos ou Metodos em comum.
    print("Criada => Definicoes Em comum a todos ")
    print("Frete km, Moto R$15.00, Carro R$30.00, Caminhao R$60.00 ")
    def ligar_motor(self):
        print(" Motor ligado")

    def dirigir(self):
        print(" Dirigindo - Mostrar Contador de tempo  ")
        print("Valor a receber")

    def freiar(self):
        print(" Freiando")

    def desligar_motor(self):
        print(" Motor desligado")
        print(" Dirigindo - Calcular tempo = Distancia  km ")
        print("Valor Total a Receber = Tempo X Frete_Veiculo ")

    # ----------------------------------------
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo): # Aqui a "classe Motocicleta " e a classe "Filha_1"
    pass

moto = Motocicleta("Ford", "Diesel","Vermelho", "dyf-84757", 10 )
moto.ligar_motor()
moto.dirigir()
moto.freiar()
moto.desligar_motor()

print(moto)

moto = Motocicleta("Roxa", "xwy-2569","Azul", "cbx-3577", 2)
print(moto)