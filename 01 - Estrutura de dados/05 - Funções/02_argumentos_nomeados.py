
# ------------- Argumentos Nomeados --------------------

# "Funcoes" Tambem podem ser chamadas usando Argumentos Nomeados Na forma "chave=valor".

# Aqui temos a funcao"def' ==>> "salvar_carro" com os Argumentos (marca, modelo, ano, placa).
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Aqui Temos # formas de passar os argumentos.
salvar_carro("Fiat", "Palio", 1999, "ABC-1234") 
# Essa e a forma mais simples e sucetivel a erros.

salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
# Essa e a forma com argumentos Melhor que a Primeira.

salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
# E Essa e a forma Mais Robusta que utiliza um dicionario "**". os Asteriscos dois ** indica que esta utilizando um dicionario.
