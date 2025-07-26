
# ----Modo mais Correto de usar metodo "Read". e "Readline"-------------

arquivo = open(
    "05 - Manipulação de arquivos\lorem.txt", "r"
)

# print(arquivo.read())  # Aqui Retorna a string inteira do Codigo.
# for linha in arquivo.readline():
for linha in arquivo.readlines():
    print(linha)

arquivo.close()

