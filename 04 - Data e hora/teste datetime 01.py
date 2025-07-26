# documentacao do python
# python.org >> docs >> docs.python.org.3/
print(" # ---1 exemplo----------------------------------" )

import datetime

d = datetime.date(2023, 7, 19) # Aqui eu declaro uma Variavel que chamei de "d" e chamo
                               #  o construtor de Data.

print(d) # Saida >>> 2023-07-19

print(" # ---2 exemplo----------------------------------" )

from datetime import date # Importando o modulo datetime

data = date(2025, 6, 9)   # Atribuindo a vatiavel "data"  o valor de "date"

print(data) # saida >>> 2025-06-09




print(" # ---3 exemplo----------------------------------" )
import datetime

d =  datetime.datetime.now()

# Formatando data e hora
print(d.strftime("%d/%m/%y %H:%M"))   # 09/06/25 20:13
print("Data e Hora Atual ==>>", d.strftime("%d/%m/%y %H:%M")) 

print("")
print(" # ---4 exemplo----------------------------------" )

# Converten do String para datetime
date_string = "20/07/2023 15:23"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)  # >>> 2025-06-09 20:23:00
print("Data e Horas definida", d) # >>> Data e Horas 2025-06-09 20:23:00

