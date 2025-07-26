
Objetivo geral
Aprender a trabalhar com gerenciamento de pacotes em python , e boas praticas de codficacao da comvencao PEP 8.

conteudo.
- gerenciamento de pacote.
- Boas preticas em python.

- Pacotes em python.
    Sao modulos de cod escritos por outras pessoas, que pode ser Instalados e utilizados em seus programas Python. Economizando tempo no seu projeto.

- PiP (pipI => Python Packarge Index) => e o Gerenciador de pacotes do python. Com Ele podemos Instalar, Atualizar, remover pacotes.

https://pypi.org/  # Endereco Oficial onde esta a maioria dos Pacotes Python

Exemplo de comandos do Pip:

pip install Numpy
pip unistall Numpy
pip list


# Commandos do pip
 Instalar um pacote
# pip install Nome_do_pacote

Desinstalar um Pacote
# pip uninstall nome_do_pacote

listar os Pacotes
# pip list

Atualizar um Pacote
# pip install --upgrade Nome_do_pacote

Procurar por pacotes
# pip search termo_de_busca






================ Uso do anbiente Virtual ================================

Ambiente virtual Criado por Venvs, Permite manter as dependencias dos projetos , evitando conflitos emtre versoes de pacotes.


Exemplo de codigo:
pytho3 -m venv myenv
source myenv/bin/activate


criando o ambiente virtual do seu projeto. dentro da pasta "Ambiente virtual"
python -m venv .env         # Esse comando cria o nosso anbiente virtual dentro da pasta.
.env\Scripts\Activate       # Esse commando ativa o anbiente virtual criado.no windows
source .env/bin/activate    # Esse commando ativa o anbiente virtual criado.no linux
ls .env                     # Esse comando lista todo os nossos pacotes dentro do nosso novo ambiente virtual.
pip list                    # Esse comando lista todos os pacotes instalados
pip                         # Mostra todos os comandos do gerenciador de Pacotes . 
Boa codificação! 🚀🐍

PS C:\Users\warp\Documents\GitHub\trilha-python-dio\05 - Manipulação de arquivos\Ambiente Virtual> python -m venv .env
PS C:\Users\warp\Documents\GitHub\trilha-python-dio\05 - Manipulação de arquivos\Ambiente Virtual> ls .env

=========================exemplo de pacote:===============================


Documentação: https://rastreio-correios.r3ck.com.br

Código Fonte: https://github.com/rennancockles/rastreio-correios

Rastreio-Correios é uma biblioteca simples para rastreamento de pacotes dos correios.

Requisitos
Uma versão recente do Python (3.8 ou superior).

Instalação
$ pip install rastreio-correios
---> 100%
Successfully installed rastreio-correios
Examplo
Para mais exemplos veja a página de funcionalidades na documentação.

from correios import Correios


correios = Correios()

objeto = correios.rastreio(cod="PM123456789BR")

if objeto and objeto.eventos:
    print(objeto.eventos[0].descricao)
Licença
Esse projeto é licenciado sobre os termos da licença MIT.

====== Gerenciadores de Pacotes Automaticos  pipenv e Poetry ===========

PoeTry e uma feramenta de gerenciamento de dependencias para Python que permite gerenciar as bibliotecas dos projetos (instalar/atualizar/remover) . Tambem suporta o empacotamento e a publicacao do projeto PypI.

# Comandos do Poetry - exemplos

Pip install poetry      # Instalando o poetry em um novo projeto "Ja existente".
poetry new myproject    # Instalando o poetry em um novo projeto do "0".
cd myproject            # Comando Para entrar na pasta do projeto exem ==> cd myproject
poetry add numpy        # Comando Para "adicionar uma dependencia"
poetry remove numpy     # Comando Para "remover uma dependencia".


black, flake8, isort

bat desafio_v1.py
flake8 --max-line-length=120 desafio_v1.py



