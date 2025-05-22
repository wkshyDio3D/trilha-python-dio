
# --------------- Metodo {}.get.py ------------------------

# o "get" e outra forma de acessar valores dentro  do dicionario.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Aqui estamos simulando um erro proposital.
# contatos["chave"]  # KeyError - Aqui retorna um erro e o programa para de rodar.


# Com o Metodo "GET" isso nao acontece.
resultado = contatos.get("chave")  # None - Aqui como nao encontrou o item "chave" retorna "none" e continua.
print(resultado)
 # >>> none

resultado = contatos.get("chave", {}) # {}  - Aqui ao nao encontrar o item "chave" esta retornado um valor definido como padrao "dicionario vazio {}" .  
print(resultado) 
 # >>> {} 

resultado = contatos.get("guilherme@gmail.com", {}) # Aqui retorna o item encontrado "guilherme@gmail.com" e nao retorna  "dicionario vazio {}" .  
print(resultado)
# >>> # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}