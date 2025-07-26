import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1
# 6_csv.py

try:
    with open(ROOT_PATH / "usuarios-2.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "lexi luna"])
        escritor.writerow(["2", "Adria Rae"])
        escritor.writerow(["3", "yenifer chacon"])
        escritor.writerow(["4", "Holly heart"])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")



