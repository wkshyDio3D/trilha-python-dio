
PEPs 8  ==>> gia de estilos para codificacao em python.

https://peps.python.org/pep-0008/

Principais recomendacoes

-- Usar 4 espacos para identaca,
-- limitar as linhas a 79 caracteres,
-- usar nomes de variaveis em ==>>  snake_case ==>>  para funcoes e variaveis.
-- usar ==>> CamelCase para classes.

exemplos:

def somar(argumento_1, argumento_2):    # snake_case ==>>  para funcoes e variaveis
    # Esta e uma funcao de exemplo seguindo a pep8
    pass
class ContaBancaria:                    # CamelCase ==>> para classes
    # Esta e uma funcao de exemplo seguindo a pep8
    pass



Usando Ferramentas de checagem de estilos pep8.

1 - flake8 mostra onde esta todas as falhas de estilos paras er corrigidas.

pip install flake8
flake8 meu_script.py


2 - Ferramentas de formatacao automatica de estilo de codigo.

pip install black
black meu_script.py


Organizacao de imports com isort.
ferramenta pythom parta Organizar automaticamente os importes.

# Criando um novo ambiente virtual
# python -m venv .env
# source .env/bin/activate

# Gerenciamento de pacotes e boas práticas\AmbienteVirtualTeste> python -m venv .env

# PS C:\Users\warp\Documents\GitHub\trilha-python-dio\06 - Gerenciamento de pacotes e 
# boas práticas\AmbienteVirtualTeste> source .env/bin/activate

# PS C:\Users\warp\Documents\GitHub\trilha-python-dio\06 - Gerenciamento de pacotes e 
# boas práticas\AmbienteVirtualTeste> pip install flake8 isort black


------------------------------------------------
exemplo de forma corretas e incorretas
Imports should usually be on separate lines:
# Correct:
import os
import sys
# Wrong:
import sys, os
It’s okay to say this though:

# Correct:
from subprocess import Popen, PIPE

import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
------------------------------------------------

instalando o isort

pip install isort
isort meu_script.py

# como instalas o insort .
# vai nas extencoes e digite "black formatter" a versao da "microsoft" e instalar 
# e depois digite "isort" da "microsoft" e instalar.
