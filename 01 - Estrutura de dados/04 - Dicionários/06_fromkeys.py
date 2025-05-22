
# --------------- Metodo {}.fromkeys.py ------------------------

# o Metodo {}.fromkeys.py cria as chaves para voce em duas situacoes.
# 1 - Quando voce quer criar as chaveis e deizar elas la vazias sem vincular nenhum valor..


resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

# 2 - Quando voce quer criar um conjunto de chaveis e quer colocar um valor padrao na chave ==>> "vazio".

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
