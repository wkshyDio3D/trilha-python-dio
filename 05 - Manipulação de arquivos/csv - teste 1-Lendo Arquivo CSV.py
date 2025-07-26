
# Lendo Arquivo CSV

import csv

with open('example.csv', 'r') as file:  # Abre o "arquivo" e joga para variavel "file".
    reader = csv.reader(file)   # Atribue uma instancai "reader" ==>> csv.reader(file)
    for row in reader:      # Aqui conseguimos ler linha a linha do nosso Arquivo
        print(row)

