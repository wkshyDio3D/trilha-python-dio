

# Exemplo de Codigo: modo de Criacao do Arquivo de 'w' Escrita. 
# file = open('exemplo.txt', 'w')
# file.write(" Ola, mundo! ")
# file.close()

# Criando o Rquivo de Escrita na Pratica.

# arquivo = open("Clicar botao direito no diretorio e copiar o caminho relativo e colar Aqui",  "w")
# arquivo = open("Clicar botao direito no diretorio e copiar o caminho relativo e colar Aqui/Nome_do_Arquivo_a_ser_Criado.txt", "w")
# Salvar e executar o Cod para que o arquivo "texte01.txt" seja criado .

# arquivo = open("C:\Users\warp\Documents\GitHub\trilha-python-dio\05 - Manipulação de arquivos",  "w")
# arquivo = open(
  #  "05 - Manipulação de arquivos/texte01.txt", "w"
   # )
# arquivo.close()

# Escrevendo no Arquivo criado "w"
arquivo = open(
    "05 - Manipulação de arquivos/texte01.txt", "w"
    )

arquivo.write(" Testando Escrita em um Novo Arquivo Criado  em 20/06/2025 as 20:52 ")
arquivo.close()