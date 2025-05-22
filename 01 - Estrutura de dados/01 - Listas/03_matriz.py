
# Listas Aninhada - Matriz Bidirecional - Colunas e Linhas

# Exemplo de Matriz Bidirecional Com 3 Linhas e 3 colunas

matriz = [
    [1, "a", 2],    # Linha 1 - col [1 => 1], [2 => "a"] e [3 => 2]
    ["b", 3, 4],    # Linha 2 - col [1 => "b"], [2 => 3] e [3 => 4]
    [6, 5, "c"]     # Linha 3 - col [1 => 6], [2 => 5] e [3 => "c"]
]

# # Acessando Dados da Listas Aninhada - Matriz Bidirecional - Colunas e Linhas

print(matriz[0])  # [1, "a", 2]     # Recuperando Todos os elementos de uma linha.
print(matriz[0][0])  # 1            # Recuperando o elemento da linha 0 - coluna 0.
print(matriz[0][-1])  # 2           # Recuperando o elemento da linha 0 - coluna 3
print(matriz[-1][-1])  # "c"        # Recuperando o elemento da ultima linha 3 - coluna 3
