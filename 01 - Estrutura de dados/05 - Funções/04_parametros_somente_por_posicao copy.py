
# -------- Parametros Especiais -----------------
# Por padrao, "argumentos" podem ser passados para uma "Funcao" ==>> "def" Tanto por "Posisao" quanto pelo "Nome" ou "ambos". 
# Dessa Forma o "Desenvolvedor " Basta apenas olhar para a definicao da "def" para saber se os itens sao passador 
# por "posicao", Por "Posicao e Nome", ou por "Nome".
# Ou Seja Parametro "com_Nome e Parametro "sem_Nome". Quando se passa Parametro "com_Nome" 
# Ou seja {"Chave":"Valor"} Sao Parametros Nomeados . 
# E Quando se passa Sequencial so com "posicao" sao parametros "Posicionais"

# def f(pos_1, pos_2, / , pos_or_Kwd, * kwd1, kwd2): 
# def f(pos_1, pos_2):  ==>> Aqui Somente por Posicao ==>> "pos_1 e pos_2".
# def f(pos_or_Kwd):    ==>> Aqui Misto ==>> "Posicao e Keyword".
# def f(pkwd1, kwd2):   ==>> Aqui Somente por posicao ==>> "Keyword_1 Keyword_2" Only

# Exemplo 1 ==>> Positional Only ou Apenas Posicional.
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Forma Correta.
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# Forma Correta.
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")

# Forma Incorreta Vai dar Erro.
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

# -------------------------------------------------------------

# Exemplo 2 ==>> Keyword only
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # Valido

# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inValido
