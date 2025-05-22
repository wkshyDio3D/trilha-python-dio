
# 01 Exemplo.

class controle_remoto:
    def ligar(self):
        print("Ligando a TV_01")
        print(" TV_01 Ligada")
       
    def desligar(self):
        print("Desligando a TV_01")
        print(" TV_01 Desligada")

class controleTV(controle_remoto):
        pass

controle = controleTV()
controle.ligar()
controle.desligar()

print("")
# 02 Exemplo.
# Criando o Modulo Abstrato com ABC
from abc import ABC, abstractmethod

class controle_remoto2(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
        

class controleTV(controle_remoto2):
    def ligar(self):
        print("Ligando a TV_02")
        print(" TV_02 Ligada")
       
    def desligar(self):
        print("Desligando a TV_02")
        print(" TV_02 Desligada")

controle = controleTV()
controle.ligar()
controle.desligar()

print("")
# 03 Exemplo. TVs e o Arcondicionado
# Criando o Modulo Abstrato com ABC

from abc import ABC, abstractmethod

class controle_remoto3(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
        

class controleTV(controle_remoto3):
    def ligar(self):
        print("Ligando a TV_03")
        print(" TV_03 Ligada")
       
    def desligar(self):
        print("Desligando a TV_03")
        print(" TV_03 Desligada")

class ControleArCondicionado(controle_remoto3):
    def ligar(self):
        print("Ligando  ArCondicionado")
        print(" ArCondicionado Ligado")
       
    def desligar(self):
        print("Desligando ArCondicionado")
        print(" ArCondicionado Desligada")


controle = controleTV()
controle.ligar()
controle.desligar()

print("")

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
# 03 Exemplo. TVs e o Arcondicionado
# Criando o Modulo Abstrato com ABC

