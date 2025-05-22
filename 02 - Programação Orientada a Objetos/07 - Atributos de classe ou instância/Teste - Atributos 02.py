

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

print("")
print("Exibindo os Alunos") 
aluno_1 = Estudante("Mackaila", 10)
aluno_2 = Estudante("Giovanna", 20)
# print(aluno_1)
# print(aluno_2)
mostrar_valores(aluno_1, aluno_2)

print("")
print("Alterando A matricula Apenas do Aluno_1")   
aluno_1.matricula = 30  # Alterando a matricula apenas do aluno_1.
mostrar_valores(aluno_1, aluno_2)

print("")
print("Alterando o Nome da Escola")
Estudante.escola = "Python" # Alterando o Nome ou 'instacia' da escola para todos os Estudantes.
aluno_1.matricula = 30
mostrar_valores(aluno_1, aluno_2)

print("")
print("Novo aluno Chappie")
aluno_3 = Estudante("Chappie", 50)

# print("")
mostrar_valores(aluno_1, aluno_2, aluno_3)

print("")
print("Exibindo Os Alunos ")
Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 50)
mostrar_valores(aluno_1, aluno_2, aluno_3)

print("")
print("Alterando a Escola Apenas do Aluno_1")
aluno_1.escola = "DIO"
aluno_3 = Estudante("Chappie", 50)
mostrar_valores(aluno_1, aluno_2, aluno_3)

print("")
print("Alterando o Nome da Escola")
Estudante.escola = "Dio_Python" # Alterando o Nome ou 'instacia' da escola para todos os Estudantes.
aluno_1.matricula = 30
mostrar_valores(aluno_1, aluno_2, aluno_3)

# Resumo: Quando Estamos Trabalhando com 'Variaveis de instancias' elas sao 'unicas por Objetos',
#  'cada objeto tem uma copia por variavel'. 
#        self.nome = nome   => 'Variaveis de instancias' => 'unicas por Objetos'
#        self.matricula = matricula

# Quando Estamos falando de 'Variaveis de classe' Essas Variaveis sao 'Unicas Para todos os Objetos'.
#   class Estudante:        
#       escola = "DIO" =>  'Variaveis de classe' -> 'Unicas Para todos os Objetos'