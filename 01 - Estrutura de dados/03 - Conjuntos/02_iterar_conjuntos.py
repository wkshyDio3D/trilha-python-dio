
# ---- Acessano ou Interando os Conjuntos dentro de um "set" com "FOR".

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

print("")

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
