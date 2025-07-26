

Para manipular Arquivos em Python, Primeiro Precisamos Abrilos. Para isso Usamos a Funcao 'open()'. Quando Terminamos de trabalhar com o arquivo , usamos a Funcao 'close()' isso libera recurso do sistema .

https://docs.python.org/3/library/csv.html

lorem ipsum ==>> textos aleatorios para teste.

exemplo:
# Aqui abrimos os arquivo de dados. .txt e .csv

Aqui passamos dois Argumentos: 1- O caminho do arquivo ==>> "example.txt"- 2- O modo de Abertura do Arquivo ==>> "r". ==>> onde "r" = modo de somente Leituta.

file = open("example.txt", "r")     # Open ==>> Abre o Arquivo
file.close()                        # close ==>> fechar o arquivo

# Aqui feichamos o arquivo de dados.

Modos de Abertura de Arquivos.
# "read" ==>> 'r' = modo de somente Leituta.
# 'w' = Gravacao 
# 'a' = anexar

Exemplos de uso de codigo:

# No modo 'r'. Utilizamos o arquivo de dados Apenas para 'leitura'.
file = open("example.txt", "r") 
file.close() 

# Para Escrever em um Arquivo.
file = open("example.txt", "w") 
file.close() 

# Para Anexar Conteudo a um arquivo ja Existente.
file = open("example.txt", "a") 
file.close() 

# ------------------------------------------------

Metodos para utilizar o ==>> Metodo 'read':

# "read()" ==>> 'r' = modo de somente Leituta.
# "readline()" ==>> 'r' = Leituta de apenas uma linha.
# "readlines()" ==>> 'r' =  Leituta de varias linhas.

1 exemplo: 
# Ler todo o conteudo do arquivo de uma vez.

file = open('example.txt', 'r')
print(file.read()) 
file.close()

 # O read vai pegar todo o conteudo do arquivo e colocar em uma 'string' e retornar. .


