
#  Colocar opção de interação com o usuário torna seu código mais dinâmico e interessante.
#  Você pode usar o input() para que a pessoa escolha:

# O nome dela. O tipo de saudação. O conteúdo que quer aprender (Java, HTML, Python...).

# Exemplo com interação no terminal:

def dizer_oi(nome): 
    return f"Oi {nome}"

def dizer_bom_dia(nome): 
    return f"Bom dia {nome}"

def dizer_hello(nome): 
    return f"Hello {nome}"

def incentivar_aprender_java(nome):
    return f"Oi {nome}, vamos aprender Java juntos!"

def incentivar_aprender_html(nome):
    return f"Bom dia {nome}, vamos aprender HTML juntos!"

def incentivar_aprender_python(nome):
    return f"Hello {nome}, vamos aprender Python juntos!"

# Menu de opções
print("Bem-vindo! Vamos montar sua mensagem personalizada.")
nome = input("Digite seu nome: ")

print("\nEscolha uma saudação:")
print("1 - Oi")
print("2 - Bom dia")
print("3 - Hello")
opcao_saudacao = input("Digite o número da saudação: ")

print("\nEscolha o que você quer aprender:")
print("1 - Java")
print("2 - HTML")
print("3 - Python")
opcao_conteudo = input("Digite o número da linguagem: ")

# Função de saudação
if opcao_saudacao == "1":
    saudacao = dizer_oi(nome)
elif opcao_saudacao == "2":
    saudacao = dizer_bom_dia(nome)
elif opcao_saudacao == "3":
    saudacao = dizer_hello(nome)
else:
    saudacao = "Saudação inválida."

# Função de incentivo
if opcao_conteudo == "1":
    incentivo = incentivar_aprender_java(nome)
elif opcao_conteudo == "2":
    incentivo = incentivar_aprender_html(nome)
elif opcao_conteudo == "3":
    incentivo = incentivar_aprender_python(nome)
else:
    incentivo = "Opção de aprendizado inválida."

# Exibir resultado
print("\nSua mensagem personalizada:")
print(saudacao)
print(incentivo)

# Resultado possível (exemplo):
# Digite seu nome: Lucas

# Escolha uma saudação:
# 1 - Oi
# 2 - Bom dia
# 3 - Hello
# Digite o número da saudação: 2

# Escolha o que você quer aprender:
# 1 - Java
# 2 - HTML
# 3 - Python
# Digite o número da linguagem: 3

# Mensagem personalizada:
# Bom dia Lucas
# Hello Lucas, vamos aprender Python juntos!