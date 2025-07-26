
# pip install pytz

from datetime import datetime

import pytz

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print("Utilizando o Modulo PYTZ Para manipulacao de time zome")
print("Europa/Oslo       ==>>> ", data)
print("America/Sao_Paulo ==>>> ", data2)
