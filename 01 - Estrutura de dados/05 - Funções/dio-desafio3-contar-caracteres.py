
print(" Digite uma frase ou palavra para ser contada as strins ok")

def contar_caracteres(string):
    # TODO: inicializar um dicionario vazio "contador" para armazenar as contagems de caracteres.:

    contador = {}


    # TODO: Intere atraves de cada cactere na string string.

    for caractere in string:

    # TODO: Para cada caractere verifique se ele ja esta presente no dicionario contador:
        if caractere in contador:
            contador[caractere] += 1

        else: 
            contador[caractere] = 1

    return contador

# Solicita a entrada do usuario.
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)