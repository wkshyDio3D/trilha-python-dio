
# ----- Metodos de Classe e Metodos Estaticos ------
   
# O que Sao e Quando sao Utilizados.
# -----   01   Metodos de Classe  ------
# 1- Metodos de Classe estao Ligados a classe e Nao ao Objeto.
#  Eles tem acesso ao estado da classe, Porque recebem um parametro 
# que aponta para a classe e nao para a instancia do objeto.
#  por exemplo o"self" aponta para a 'instancia da classe' que seria o 'Objeto'.
# Quando Definimos o metodo de Classe 'cls', Que ao inves de apontar para a instancia do Objeto
#  ele aponta diretamente para minha Classe e por convencao ele e chamado de 'cls'.



# # -----  02   Metodos Estaticos ------
# 2 - Metodo  Estatico nao recebe um primeiro Argumento explicito. Ele esta vinculado
#  a classe e nao ao objeto da classe. Esse Metodo nao pode acessar ou modificar 
# o estado da classe. E esta presente em uma classe porque faz sentido que esteja
#  presente na classe.

# -----  Metodo de classe X Estaticos   ---
# Um metodo de classe recebe um Primeiro parametro que aponta para a classe, 
# Enquanto o metodo estatico Nao. 
# Um Metodo de classe pode acessar ou Modificar o Estado da classe ,
#  Enquanto o metodo estatico nao pode acessa-lo ou modifica-lo.
  
# --- Quando Utilizar Metodos de Classe ou Estaticos 
# Usamos Metodos de classe Para criar Metodos de fablica.
# Usamos Metodos Estaticos para  criar funcoes Utilitarias.

# Metodos de Fabrica. Sao metodos que retorna Instancias daquela classe

print(" 1 Exemplo . ") 
class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        pass
p = pessoa("SisiDiamind", 28)
print(p.nome, p.idade)

print("")

print(" 2 Exemplo . Nesse metodo prescisamos instanciar") 
class pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        pass

    def criar_apartir_data_nascimento(self, ano, mes, dia, nome):
        idade = 2025 - ano
        return pessoa(nome, idade)
    
# p = pessoa("SisiDiamind", 28)
# print(p.nome, p.idade)

p2 = pessoa().criar_apartir_data_nascimento(1962, 10, 28, "SisiDiamind")
print(p2.nome, p2.idade)

print("")

print(" 3 Exemplo .  'metodo de class' correto que nao prescisa instanciar") 
class pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
p2 = pessoa.criar_apartir_data_nascimento(1962, 10, 28, "SisiDiamind")
print(p2.nome, p2.idade)

print("")

print(" 4 Exemplo .  'metodo de Estatico' ") 
class pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod # Declarando o Metodo de 'Class'
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod   # Declarando o Metodo de 'statico'
    def e_maior_idade(idade):
        return idade >= 18
    
 # Chamando o metodo class.   
p2 = pessoa.criar_apartir_data_nascimento(1962, 10, 28, "SisiDiamind")
print(p2.nome, p2.idade)

# Chamando o metodo Estatico.
# pessoa.e_maior_idade(18)
# pessoa.e_maior_idade(28)

print(pessoa.e_maior_idade(18))
print(pessoa.e_maior_idade(17))
print(pessoa.e_maior_idade(28))

