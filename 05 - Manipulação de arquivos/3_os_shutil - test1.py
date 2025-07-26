
# Exemplo de Codigo de Gerenciamento de aArquivos em python

import os
import shutil
# from pathlib import Path

# ROOT_PATH = Path(__file__).parent

# Criar um Diretorio.
# os.mkdir("exemplo")
os.mkdir(ROOT_PATH / "novo-diretorio")


# Abrir um Arquivo.
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

# Renomear um Arquivo.
# os.rename("old.txt", "new.txt")
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# Remover um Arquivo.
# os.remove(ROOT_PATH / "alterado.txt")
os.remove(ROOT_PATH / "alterado.txt")

# Mover um Arquivo
# shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")