

class Estudante:        # Classe 'Estudande'
    escola = "DIO"      # Atributo 'Escola' -> Atribuicao 'DIO'

    def __init__(self, nome, matricula): # Aqui Temos o Construtor -> e Os -> atributos do 'Estudante.
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str: # Aqui tremos o metodo '__str__' Para fazer a representacao da Classe de Estudante.
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

# Aqui Estamos Instanciando Os Dois estudantes. Com Seus Atributos.
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
