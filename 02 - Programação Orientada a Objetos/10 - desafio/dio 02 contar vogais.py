
def contar_vogais(texto):
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    # TODO: Defina um conjunto de vogais tanto minuscula quanto Maiusculas:

    # TODO: Inicialize um contador para contar as vogais:
    contador = 0

    # Iteramos pelos caracteres da string.
    for char in texto:
        # TODO: Verifique se o caractere atual e uma vogal e incremente o valor do contador:
        if char in vogais:
            contador +=1

    return contador

# Solicita ao usuario que insira uma string.
texto = input("Insira uma String?")

# Chama a funcao contar_vogais(texto) e exibe o resultado.
resultado = contar_vogais(texto)
print(f"O numero de vogais na istring '{texto}' e: {resultado}")
