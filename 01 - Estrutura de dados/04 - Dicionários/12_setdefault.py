
# --------------- Metodo {}.setdefault.py ------------------------

# O setdefaul ==>> utilizado para caso voce queira adicionar um item ao seu dicionario mais
#  voce nao sabe se ele ja existe ou nao no seu dicionario e voce nao quer perder tempo procurando.
# Se o item nao existir ele escreve um novo item . se ja existir ele nao sub-escreve o item preservando o original.


contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
