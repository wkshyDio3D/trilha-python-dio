
class pessoa1:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        pass

# Entrada do Usuario
nome = input(" Qual o seu Nome")
idade = int(input(" Qual a sua Idade ? "))

# Criando a instacia da pessoa
pessoa = pessoa1(nome, idade)
print("Nome:", pessoa.nome, "Idade:", pessoa.idade)

print("")

# ------------------------------------

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self): # Metodo Para Retornar as informacoes Formatada
        return f"Nome: {self.nome}, Idade: {self.idade}"

# Entrada do Usuario
nome = input(" Qual o seu Nome")
idade = int(input(" Qual a sua Idade ? "))

# Criando a instacia da pessoa
pessoa = Pessoa(nome, idade)

# Chamando o Metodo e imprime o resultado
print(pessoa.apresentar())

# ------------------------------------
class calculadora:
    # Metodo para somar dois numeros.
    def soma(self, a, b):
        return a + b

# Entrada dos Dois Numeros Inteiros
num1 = int(input(" Informe o Primeiro Numero :"))
num2 = int(input(" Informe o Segundo Numero :"))

# Criando a Instancia da Calculadora.
calc = calculadora()

# Exibindo os Resultados das Operacoes.
resultado = calc.soma(num1, num2)
print("Total : ", resultado)