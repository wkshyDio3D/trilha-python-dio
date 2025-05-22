
# --------------- Metodo {}.keys.py ------------------------

# Retorna so as chaveis do nosso dicionario.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

print("------------------------------")
resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado) # Aqui Vai mostrar a chave. >>> dict_keys(['guilherme@gmail.com'])

# Criando novas chaveis .
novo_dicionario = {"a": 100, 1: "teste-1", "b": "python", 2: "teste-2" }
print(novo_dicionario) # Aqui mostra todas as chaveis e seus valores.

print("------------------------------")
print(novo_dicionario.keys()) # Aqui Vai mostrar apenas as chaveis. >>> dict_keys(['a', 1, 'b', 2])
