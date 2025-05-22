
# --------------- Metodo {}.Copy.py ------------------------

# Com O metodo Copy Criamos uma copia identica porem em uma instacia diferente . 
# Isso significa que o que for auterado na copia nao interfere na Principau.ok
# Vamos utilizar o metodo COPY quando presisamos manipular o dicionario ,mais nao queremos auterar o original.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}
