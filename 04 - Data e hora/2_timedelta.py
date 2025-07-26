from datetime import date, datetime, timedelta

# Aqui determona o tempo estimado "Pequeno, Medio ou Grande"
# tipo_carro = "P"  # P, M, G
tipo_carro = "M"  # P, M, G
# tipo_carro = "G"  # P, M, G

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual - timedelta(days=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual - timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual - timedelta(days=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


print(date.today() - timedelta(days=1)) # Aqui estamos decrementando um dia 

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1) # Aqui estamos decrementando uma hora 
print(resultado.time())

print(datetime.now().date())
