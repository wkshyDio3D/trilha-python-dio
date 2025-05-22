
# ---------- Tuplas aninhadas -----------------------

# TUPLAS podem armazenar todos os tipos de objetos em Python, podemos 
# ter TUPLAS que armazenam TUPLAS. 
# Podemos assim criar estruturas bidimencionais(Tabelas), com linhas e colunas.
# E acessar as informacoes utilizando indices de linhas e colunas.

# Exemplo:
matriz = (
    (1, "a", 2),    # Linha 1 ou tupla 1   e colunas 0 - 1 - 2
    ("b", 3, 4),    # Linha 2 ou tupla 2   e colunas 0 - 1 - 2
    (6, 5, "c"),    # Linha 3 ou tupla 3   e colunas 0 - 1 - 2
)

print(matriz[0])          # Informando apenas o indice [0] retorna todos os objetos da linha 1. 
# >>> # (1, "a", 2) 

print(matriz[0][0])       # Informando apenas o indice [0] linha [0] retorna o objeto do indice [0].
 # 1

print(matriz[0][-1])    # Informando apenas o indice [0] linha [-1] retorna o objeto do indice [2].
 # 2

print(matriz[-1][-1])
# "c"

# Utilizamos tuplas ao inves de listas quando queremos ter a garantia, 
# que os valores nao serao auterados,
