

# Metodo Read: metodos de leitura de Arquivos .txt

# 1 exemplo: 
# Ler todo o conteudo do arquivo de uma vez.

file = open('example.txt', 'r')
print(file.read()) 
file.close()