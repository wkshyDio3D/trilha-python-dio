import os
import shutil
from pathlib import Path

# Esse coma mando identifica automaticamente o diretorio que queremos utilizar.
ROOT_PATH = Path(__file__).parent 
print(ROOT_PATH.parent)
# ===>> "c:/Users/warp/Documents/GitHub/trilha-python-dio/05 - Manipulação de
#  arquivos/3_os_shutil - diretorio test2.py" 

# Criando Nosso, "Novo-Diretorio_2".
# os.mkdir(ROOT_PATH / "novo-diretorio-2")

# Criando nosso "novo-arquivo-1" no nosso "Novo-diretorio-2".
arquivo = open(ROOT_PATH / "novo-arquivo-1.txt", "w")
arquivo.close()

# Renomeando Arquivo "novo.txt" para "alterado.txt"
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# Removendo o Arquivo "alterado.txt"
os.remove(ROOT_PATH / "alterado.txt")

# Movendo o Arquivo "novo.txt" para outro Diretorio "novo-diretorio" / "novo.txt"
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")