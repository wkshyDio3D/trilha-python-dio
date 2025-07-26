
# ----- Modo mais simples de usar o metodo "Read". e "Readline" -----
arquivo = open(
    "05 - Manipulação de arquivos\lorem.txt", "r"
)

# print(arquivo.read())  # Aqui Retorna a string inteira do Codigo.

# readline()) # Aqui Retorna Apenas uma linha por vez.
# print(arquivo.readline()) #  ==> aqui retorna a 1-linha

print(arquivo.readline()) #  ==> aqui retorna a 1-linha
print(arquivo.readline()) #  ==> aqui retorna a 2-linha
print(arquivo.readline()) #  ==> aqui retorna a 3-linha

arquivo.close()

# ----Modo mais Correto de usar metodo "Read". e "Readline"-------------