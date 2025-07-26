
Trabalhando e manipulando arquivo CSV.
Abrir - Criacao - Leitura - Escrita

Introducao 
    CSV ==>> 'Comma Separated Values'. ou seja 'Valores Separados por Virgula'.
obs. Tambem pode utilizar o ==>> ';' para separar valores.

    CSV e um Arquivo de texto com formato para segmentar os dato de forma tabular.
Amplamente utilizado para armazernar Dados Tabulares. 

Lendo arquivos CSV
    O Python fornece um modulo chamado 'CSV' para lidar com Arquivos CSV.

1° Exemplo de Codigo CSV:   Lendo Arquivo CSV
=============================================

import csv

with open('example.csv', 'r') as file:  # Abre o "arquivo" e joga para variavel "file".
    reader = csv.reader(file)   # Atribue uma instancai "reader" ==>> csv.reader(file)
    for row in reader:      # Aqui conseguimos ler linha a linha do nosso Arquivo
        print(row)

----------------------------------------------------------------------------------------

2° Exemplo de Codigo CSV:   Escrevendo Arquivo CSV
==================================================

# Escrevendo Arquivo CSV

import csv

with open('example.csv', 'w', newline='') as file:
    write = csv.writer(file)
    write.writerow(["Nome", "Idade"])
    write.writerow(["Ana", 30])
    write.writerow(["Joao", 25])

----------------------------------------------------------------------------------------

Praticas CSV recomendadas

- Usar CSV.reader e CSV.writer para manipular arquivos CSV.
- Fazer o tratamento correto de execoes.
- Ao gravar arquivos CSV definir o argumento newline='' no metodo 'open'.

--------Criando um novo arquivo CSV------Passo a passo--------------------------------

1. criando o tratamento de erro.

import csv
try:
    pass
except IOError as exc:
    print(f'erro ao criar o arquivo. {exc}')

2. 

import csv
try:
    pass
except IOError as exc:
    print(f'erro ao criar o arquivo. {exc}')




