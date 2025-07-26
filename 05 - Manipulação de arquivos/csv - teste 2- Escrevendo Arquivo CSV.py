

# Escrevendo Arquivo CSV

import csv

with open('example.csv', 'w', newline='') as file:
    write = csv.writer(file)
    write.writerow(["Nome", "Idade"])   # Aqui  Monta o cabecalho do nosso Arquivo.
    write.writerow(["leah gotti", 30])         # Aqui Passamos os valores.
    write.writerow(["Holly heart", 25])        # Aqui Passamos os valores.
    write.writerow(["Adria Rae", 25])        # Aqui Passamos os valores.