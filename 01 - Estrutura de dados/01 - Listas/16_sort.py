
# ---------Comando [] SORT -------------------
# Utilizado para Ordenar uma lista .

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)
# sort() ==>> Aqui a lista esta Ordenada de forma alfabetica.


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)
# sort(reverse=True) ==>> Aqui a lista esta Ordenada Na forma Inversa.


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)
# sort(key=lambda x: len(x)) Aqui a lista esta Ordenada por tamanho da string.
# Nesse caso da menor "c" para a maior "csharp".


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
# sort(key=lambda x: len(x), reverse=True) Aqui a lista esta Ordenada inversamente da maior para a menor
# e na forma inversa a anterior. 