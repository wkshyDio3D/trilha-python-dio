
 # Definindo a classe Calculadora.
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
print(resultado)

# Resumo : A classe Calculadora possui o metodo "Soma", que recebe 
# Dois parametros (a e b) e retorna a soma deles.
# O program le os dois numeros Inteiros  do usuario, Cria Uma
#  Instacia da Calculadora, e chama o Metodo "Soma" e Imprime o Resultado.si