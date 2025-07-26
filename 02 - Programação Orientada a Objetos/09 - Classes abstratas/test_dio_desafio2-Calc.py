


 # Definindo a classe Calculadora.
class calculadora: # Metodo para somar dois numeros.
   
    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
            return "Erro: Divisao por Zero !"
        return a / b


# Entrada dos Dois Numeros Inteiros
num1 = int(input(" Digite o Primeiro Numero :"))
num2 = int(input(" Digite o Segundo Numero :"))

# Criando a Instancia da Calculadora.
calc = calculadora()

# Exibindo os Resultados das Operacoes.
resultado = calc.soma(num1, num2)
print(resultado)

print("Soma:", calc.soma(num1, num2))
print("Subtracao:", calc.subtracao(num1, num2))
print("Multiplicacao:", calc.multiplicacao(num1, num2))
print("Divisao:", calc.divisao(num1, num2))
