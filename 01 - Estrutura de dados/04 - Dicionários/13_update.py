
# --------------- Metodo {}.update.py ------------------------

# 

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}       # ==>> Original 
print(contatos) # {'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})                                # ==>> Primeiro Update
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})   # ==>> Segundo Update
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
