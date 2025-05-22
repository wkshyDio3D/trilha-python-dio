


# -------- Heranca Siples ------------

# Exemplo ==>> Sintaxe da Herenca simples
class a:    # Classe "a", e a classe => Mae.
    print(" Classe Mae ")
    pass
class b(a): # Aqui a Classe "b" ou "Classe filha" Herda da classe "a" ou "classe Mae".
    print(" Classe Filha ")
    pass
# Fim Exemplo ==>> Sintaxe da Herenca simples

class Veiculo: # Aqui a "classe Veiculo" e a classe "Mae"
    def __init__(self, cor, placa, numero_rodas):   # Aqui Temos as caracteristicas em comum a todos.
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    # Agora Vamos definir os comportamentos ou Metodos em comum.
    def ligar_motor(self):
        print(" Ligando o motor ")
        print("")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta_1(Veiculo): # Aqui a "classe Motocicleta " e a classe "Filha_1"
    pass

class Motocicleta_2(Veiculo): # Aqui a "classe Motocicleta " e a classe "Filha_1"
    pass


class Carro(Veiculo):   #  Aqui a "classe Carro " e a classe "Filha_2"
    pass


class Caminhao_1(Veiculo):    # Aqui a "classe Caminhao " e a classe "Filha_3"
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas) # Aqui Estamos Invocando um metodo da classe Pai.
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

class Caminhao_2(Veiculo):    # Aqui a "classe Caminhao " e a classe "Filha_3"
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas) # Aqui Estamos Invocando um metodo da classe Pai.
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta_1("preta", "abc-1234", 2)
moto.ligar_motor()



carro = Carro("branco", "xde-0098", 4)
carro.ligar_motor()


# caminhao = Caminhao("roxo", "gfd-8712", 8, True)
caminhao = Caminhao_1("roxo", "gfd-8712", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()

caminhao = Caminhao_2("Vermelho", "fhy-8643", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(moto)
print(carro)
print(caminhao)

moto = Motocicleta_2("Roxa", "xwy-2569", 3)
print(moto)