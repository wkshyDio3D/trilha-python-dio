

class ConversorTemperatura:
    # Metodo que Realiza a conversao de celsius para fahrenheit.
    def celcius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32
    
# Entrada do Usuario.
celsius = float(input("Qual a Temperatura em graus Celsius? "))

# Criando a Instancia do conversor.
conversor = ConversorTemperatura()

# Chamando o Metodo de conversao e imprimindo resultado.
fahrenheit = conversor.celcius_para_fahrenheit(celsius)

print(fahrenheit)

print(" Celsius ", celsius, " = ", " fahrenheit ", fahrenheit)