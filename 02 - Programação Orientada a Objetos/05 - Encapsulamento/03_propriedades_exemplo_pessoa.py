class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    # @property
    # def nome(self):
      #  return self._nome   

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento
    
    # def get_nome(self):        # Esse cod e usado em Jave c++ 
      #  return self._nome
    
    # def get_idade(self):      # Esse cod e usado em Jave c++ 
      #  return 2022 - self._ano_nascimento


pessoa = Pessoa("Guilherme", 1962)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")   # "Tabulacao ==>> '\t'

# print(f"Nome: {pessoa.get_nome()} \tidade: {pessoa.get_idade()}") # Esse cod e usado em Jave c++ 

