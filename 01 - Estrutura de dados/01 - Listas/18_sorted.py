
# --------------- Funcao [] Sorted -----------

# Basicamente que o comando "SORT" com a diferenca e que o "sorted" e uma funcao .

linguagens = ["python", "js", "c", "java", "csharp"]
print(sorted(linguagens))
# >>> ['c', 'csharp', 'java', 'js', 'python']


print(sorted(linguagens, key=lambda x: len(x)))  
# >>>  ["c", "js", "java", "python", "csharp"]

print(sorted(linguagens, key=lambda x: len(x), reverse=True))  
# >>>  ["python", "csharp", "java", "js", "c"]



