
# --------------- Metodo {}.popitem.py ------------------------

# Popitem - Quando nao e informado qual e a chave ele vai removendo os itens na sequencia 

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)
print("Removidos : ", resultado)


# contatos.popitem()  # KeyError
