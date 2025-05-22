
# --------------- Metodo {}.items.py ------------------------

# Retorna uma lista de tuplas do nosso dicionario.
# Muito util quando quer utilizar o comando for para interar.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
print(resultado)
