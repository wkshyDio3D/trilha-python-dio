
command ==>> pwd                             ==>> para entrar no diretorio atual...
command ==>> mkdir "01-AmbienteVirual"    ==>> Cria o Novo Ambiente Virtual ".env"
command ==>> cd\ 01-AmbienteVirual         ==>> cd\ para entrar no diretorio 
command ==>> deactivate                   ==>> Desativa o Ambiente Virtual ".env" 

command ==>> pip list                      ==>> Lista todos os pacotes instalados
================ Uso do anbiente Virtual ================================

Ambiente virtual Criado por Venvs, Permite manter as dependencias dos projetos , evitando conflitos emtre versoes de pacotes.


Exemplo de codigo:
pytho3 -m venv myenv
source myenv/bin/activate

O ambiente Virtual deve ser criado na pasta Raiz de cada seu Novo  Projeto.

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
