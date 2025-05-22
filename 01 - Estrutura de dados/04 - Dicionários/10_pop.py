
# --------------- Metodo {}.pop.py ------------------------

# O POP vai remover e retornar ou mostrar o valor que removeu.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
print(contatos)
print("Valores do contato: ",contatos) # Aqui mostra todos os contatos.

resultado = contatos.pop("guilherme@gmail.com") 
print(resultado)
print("Valores Removidos : ", resultado) # Aqui vai mostrar os valores da chave Removido.
# >>>  # {'nome': 'Guilherme', 'telefone': '3333-2221'}


resultado = contatos.pop("guilherme@gmail.com", {})  
print(resultado) # {} 
# ou
resultado = contatos.pop("guilherme@gmail.com", "Nao encontrado")  
print(resultado) # {} 




