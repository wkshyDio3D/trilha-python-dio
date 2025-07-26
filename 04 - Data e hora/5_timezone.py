from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print("Utilizando o Modulo DATETIME Para manipulacao de time zome")
print(data_oslo)
print(data_sao_paulo)

print("")


data_oslo = datetime.now(timezone(timedelta(hours=2), "OSL"))
print("Europe_Oslo     ==>> ", data_oslo)
print("America Sao Paulo ==>> ", data_sao_paulo)