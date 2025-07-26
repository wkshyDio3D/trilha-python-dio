
Gerenciamento de Pacotes com Pipenv ou Poetry 

http://pipenv.pypa.io/en/latest/

https://python-poetry.org/docs/

Gerenciamento de Pacotes com Pipenv.

Objetivo:
Aprender a trabalhar com Gerenciamento de Pacotes de Acordo com a convencao PeP8.

- Pacotes em python.
    Sao modulos de cod escritos por outras pessoas, que pode ser Instalados e utilizados em seus programas Python. Economizando tempo no seu projeto.

# Comandos do Pipenv

pip install pipenv          # instalar o "Pipenv" globalmente sem estar dentro do
                            #    ambiente virtual
pipenv install numpy        # Instalando o pacote do "numpy"
pipenv unistall numpy       # Desinstalando o pacote do "numpy"
pipenv lock                 # 

 ==>> pip list                      ==>> Lista todos os pacotes instalados
 ==>> pipenv                      ==>> Mostra help com todos os comando do pipenv
 ==>> pipenv install django         ==>> Instalando o "django" com o pipenv

==>> ls                           ==>> lista os arquivos na rais do nosso projeto
                                    apos a instalacao do Django mostra dois novos arquivos "pipfile" e "pipfile.lock".

==>> bat pipfile
==>> pipenv lock                ==>> gera e Atualiza o arquivo de lock
==>> ls                            ==>> mostra os arquivos instalados.
==>> rm pipfile.lock            ==>> Remove o C
==>> ls                            ==>> mostra arquivos "pipfile.lock" foi removidos
==>> pipenv lock                ==>> Instalando novamente o ==>> pipenv lock
==>> ls                             ==>> mostrao arquivo ==>> pipenv lock foi instalado

==>> pipenv graph               ==>> Lista Todas as dependencias aninhadas.
==>> pipenv unistall django      ==>> Desinstalando django
==>> pipenv clean              ==>> Desindtala todas as dependecias instaladas

-------------------------------------------------------------------------------------

Gerenciamento de Pacotes com  Poetry 

https://python-poetry.org/docs/

====== Gerenciadores de Pacotes Automaticos  pipenv e Poetry ===========

PoeTry e uma feramenta de gerenciamento de dependencias para Python que permite gerenciar as bibliotecas dos projetos (instalar/atualizar/remover) . Tambem suporta o empacotamento e a publicacao do projeto PypI.

Assim como o pipenv o poetry deve ser instalado globalmente.

 
# Comandos do Poetry - exemplos

Pip install poetry      # Instalando o poetry em um novo projeto "Ja existente".
poetry new myproject    # Instalando o poetry em um novo projeto do "0".
cd myproject            # Comando Para entrar na pasta do projeto exem ==> cd myproject
poetry add numpy        # Comando Para "adicionar uma dependencia"
poetry remove numpy     # Comando Para "remover uma dependencia".


black, flake8, isort

bat desafio_v1.py
flake8 --max-line-length=120 desafio_v1.py

instalando  "poetry" passo a passo 

ls

pip install poetry      # instalamdo o poetry

poetry new myproject    # Instalando o poetry em um novo projeto do "0".

poetry init             # Iniciando o novo ambiente virtual criado

This command will guide you through creating your pyproject.toml config.
Package name [01-ambientevirual]:  


Package name [01-ambientevirual]:  
Version [0.1.0]:  
Description []:  
Author [wkshydio3d <wkshy3d@gmail.com>, n to skip]:  
License []:  
Compatible Python versions [>=3.13]:  

Would you like to define your main dependencies interactively? (yes/no) [yes]


==>> definindo o django como dependencias...
Package to add or search for (leave blank to skip):
Package to add or search for (leave blank to skip): django

==>> Nas opicoes encontradas escolha a primeira [0] ok

Enter package # to add, or the complete package name if it is not listed []:
 [ 0] django
 [ 1] 
 >

Enter package # to add, or the complete package name if it is not listed []:
 [ 0] django
 [ 1] 
 > 0        <<===

Enter the version constraint to require (or leave blank to use the latest version): 
Using version ^5.2.4 for django

Add a package (leave blank to skip): 

==>> Aqui nessa opicao defina como "no" senao ele vai usar o "yes" como opcao
Would you like to define your development dependencies interactively? (yes/no) [yes]
Would you like to define your development dependencies interactively? (yes/no) [yes] no <<== Enter

==>> Exemplo com Resumo de como vai ficar a configuracao final .

[project]
name = "01-ambientevirual"
version = "0.1.0"
description = ""
authors = [
    {name = "wkshydio3d",email = "wkshy3d@gmail.com"}
]
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "django (>=5.2.4,<6.0.0)"
]


[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"

==>> Defina como "yes" se estiver tudo ok
Do you confirm generation? (yes/no) [yes]
Do you confirm generation? (yes/no) [yes] yes   <<== Enter

ls      ==>> ls  ==>> vai mostrar como ficou a "home"

    arquivos\01-AmbienteVirual


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          7/9/2025   8:02 PM                myproject
-a----          7/9/2025   8:18 PM            354 pyproject.toml

------------------------------------------------------
     Esse e o conteudo do nosso "pyproject.toml".
------------------------------------------------------

[project]
name = "01-ambientevirual"
version = "0.1.0"
description = ""
authors = [
    {name = "wkshydio3d",email = "wkshy3d@gmail.com"}
]
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "django (>=5.2.4,<6.0.0)"
]


[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"

----------------------------------------------------------------

Agora com o Poetry instalado e configurado podemos iniciar a criar o nosso novo ambiente virtual..

 poetry install

---------------------------------
 Updating dependencies
Resolving dependencies... (1.1s)    

No dependencies to install or update

Writing lock file

Installing the current project: 01-ambientevirual (0.1.0)
---------------------------------------------------------

poetry           # Mostrar o help

poetry show     # mostra mostra os pacotes que estao instalados..

asgiref  3.9.1  ASGI specs, helper code, and adapters
django   5.2.4  A high-level Python web framework that encourages rapid development and cl...
sqlparse 0.5.3  A non-validating SQL parser.
tzdata   2025.2 Provider of IANA time zone data

poetry show --help      # mostar Todos os comando do --help

 poetry show -t         # mostar as dependencias em Arvore "tree".
django 5.2.4 A high-level Python web framework that encourages rapid development and clean, pragmatic design.
├── asgiref >=3.8.1
├── sqlparse >=0.3.1
└── tzdata *

----------------Removendo os pacotes------------------------------

poetry remove django

==>> Arquivos Removidos
Package operations: 0 installs, 0 updates, 4 removals

  - Removing asgiref (3.9.1)
  - Removing django (5.2.4)
  - Removing sqlparse (0.5.3)
  - Removing tzdata (2025.2)

-----------------------------------------------------
  poetry show -t    # Mostra que todos os arquivos dependentes foram removidos.

  https://python-poetry.org/docs/