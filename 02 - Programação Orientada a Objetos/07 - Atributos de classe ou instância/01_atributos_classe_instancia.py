
# ----- Variavais de Classe e Variaveis de Instancias ----

# O que Sao e como Utilizar.
# Todos os Objetos Naicem com o mesmo Numero de atributos de classe e de instancia. 
# Os Atributos de Instancias sao diferentes para cada Objeto(Cada Objeto tem uma copia),
#  ja os atributos de Classe sao compartilhados entre os Objetos.

class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
