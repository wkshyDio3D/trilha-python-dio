
# ----------- Comando [] REMOVE ------------------

# Utilizado para remover um objeto diretamente pelo nome do objeto .
# O REMOVE vai remover um objeto de cada vez . Se tiver mais de uma 
# ocorrencia do mesmo objeto tera que fazer uma logica com o "count"
#  para remover mais objetos ate zerar ok.


linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens)  # ['python', 'js', 'c', 'java', 'csharp']

linguagens.remove("java")
print(linguagens)  # ['python', 'js', 'c', 'csharp']
