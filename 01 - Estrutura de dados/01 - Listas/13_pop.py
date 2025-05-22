
# --------- Comando [] POP ----------------------------

# Utilizando uma pilha de pratos para exemplificar o uso do comando "POP"

# primeiro prato  ==>> primeiro "elemento"
# segundo prato   ==>> segundo "elemento"
# terceiro Prato  ==>>  terceiro "elemento"
# Quarto prato    ==>> quarto "elemento"
# quinto Prato    ==>>  quinto e ultimo "elemento" da nossa lista.

# Por padrao o POP no Python Remove u ultimo elemento da pilha de pratos.

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.pop())  # Aqui o POP removeu o ==>> csharp 
print(linguagens.pop())  # Aqui o POP removeu o ==>> java
print(linguagens.pop())  # Aqui o POP removeu o ==>> c
print(linguagens.pop(0))  # Aqui o POP removeu o ==>> python na Posicao "0"

print(" ------------------------------------")

# Aqui na forma detalhada do usso do []"POP"
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.pop())  # Aqui o POP removeu o ==>> csharp 

linguagens = ["python", "js", "c", "java"]
print(linguagens.pop())  # Aqui o POP removeu o ==>> java

linguagens = ["python", "js", "c"]
print(linguagens.pop())  # Aqui o POP removeu o ==>> c

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.pop(0))  # Aqui o POP removeu o ==>> python na Posicao "0"

# Ou seja Tambem podemos utilizar o POP para remover um item especifico 
# determinando o index da sua posicao. 


# linguagens = ["python", "js", "c", "java", "csharp" , 2025, "wsh"]