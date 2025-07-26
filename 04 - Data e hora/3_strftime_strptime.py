from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-07-18 19:23:17"
mascara_ptbr = "%d/%m/%Y %a"   # Formato = Dia -Mes- Ano- em ptbr
mascara_en = "%Y-%m-%d %H:%M:%S"  # Formato = Dia -Mes- Ano- em en

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)

print(data_convertida)
print(type(data_convertida))

print(" # Trazendo so o Ano convertido.")
print(data_convertida.strftime("%Y")) 
print(" # Trazendo so o Ano e Mes convertido.")
print(data_convertida.strftime("%Y-%m")) 

print(" # Trazendo so o Mes convertido.")
print(data_convertida.strftime("%m")) 

print(" # Trazendo so o dia convertido.")
print(data_convertida.strftime("%d")) 

print(" # Trazendo so a Horas convertido.")
print(data_convertida.strftime("%H"))

print(" # Trazendo so o Minutos convertido.")
print(data_convertida.strftime("%M"))

print(" # Trazendo so o segundos convertido.")
print(data_convertida.strftime("%S"))
