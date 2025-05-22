
# -------- Usando O Comando []"Extend" ----------------------

# Usado para ao Inves de adicionar objetos a minha lista um a um como no comando "Append" 
# Aqui podemos por exemplo juntar duas ou mais listas diferentes em uma unica lista


linguagens = ["python", "js", "c"] 
# Essa e a lista alvo original.

print(linguagens)  
# >>> ["python", "js", "c"]

linguagens.extend(["java", "csharp", "2025", "wash"])
# Essa e nova lista que sera adicionmada a lista original. 

print(linguagens)  
# Esse e o resultado da juncao das duas listas.
# >>> ['python', 'js', 'c', 'java', 'csharp', '2025', 'wash']
