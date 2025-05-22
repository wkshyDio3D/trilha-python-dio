
# ---------------- Comando [] Index ----------------

# Quando eu quero saber por exemplo, qual e a posicao da primeira Ocorencia
#  do objeto "java" na minha lista.

  # posisoes    0     -  1  -  2 -    3  -    4    -  5  -   6  -   7
linguagens = ["python", "js", "c", "java", "csharp", 1914, "wsh", "java" ]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

print(linguagens.index(1914))  # 5
print(linguagens.index("wsh"))  # 6

# Obs. O Index nao vai mostar todas as posicoes da ocorrencia do objeto "java" , 
# somente a primeira posicao da ocorencia ok