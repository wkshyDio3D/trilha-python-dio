

class Veiculo: # Aqui a "classe Veiculo" e a classe "Mae"
    def __init__(self, cor, placa, numero_rodas):   # Aqui Temos as caracteristicas em comum a todos.
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    # Agora Vamos definir os comportamentos ou Metodos em comum.
    def ligar_motor(self):
        print("Ligando o motor")


# Aqui a "classe Motocicleta " e a classe "Filha_1".  
class Motocicleta(Veiculo): 
    pass

 #  Aqui a "classe Carro " e a classe "Filha_2".
class Carro(Veiculo):  
    pass

# Aqui a "classe Caminhao " e a classe "Filha_3".
class Caminhao(Veiculo):    
    pass

# Aqui vamos pasar as caracteristicas definidas na ==> Class Veiculo. que sao ==>a "cor", a "placa", e o "numero_rodas".
moto = Motocicleta("Preta", "was-3876", 2)  