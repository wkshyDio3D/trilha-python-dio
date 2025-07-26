

Desafio - Manipulacao de arquivo.

O Decorador deve registrar o segunte para cada chamada de funcao:
1 - Data e Hora atuais.
2 - Nome da Funcao.
3 - Argumento da Funcao.
4 - Valor retornado da Funcao.
5 - O Arquivo de Log deve ser chamado 'log.txt'.
6 - Se o Arquivo de log.txt ja existir, os novos logs devem ser adicionados ao final do arquivo.
7 - Cada emtrada de log deve estar em uma nova linha.


1 - Data e Hora atuais.

   def log_transacao(func):
    def envelope(*args, **kwargs):
4==>>   resultado = func(*args, **kwargs)
1=>>    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # TODO: alterar a implementação para salvar em arquivo.

       1==>"data e hora"  2==>> "Nome da funcao"        3==>> Argumento da Funcao.       4==>> Valor retornado da Funcao.
2=>>    # f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. Retornou {resultado}\n"

        print(f"{data_hora}: {func.__name__.upper()}")
4==>>        return resultado

# ===================Usando o metodo ==>> open() e close()==========================

# -------5 -Criando o Arquivo de Log chamado 'log.txt'.------------------------
def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#        arquivo = open('log.txt') # 5==>> Criando o Arquivo de log.txt no modo "a" de anexar 

        # TODO: alterar a implementação para salvar em arquivo.
        # f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. Retornou {resultado}\n"
        print(f"{data_hora}: {func.__name__.upper()}")

#       arquivo.close()  # 5==>> fechando o arquivo de log.txt

        return resultado

# ================Usando o metodo == >> with ==>> open() e close()==========================

# -------5 -Criando o Arquivo de Log chamado 'log.txt'.--com metodo with opem--------------------
def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#        with open("log.txt", "a") as arquivo:
#           f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. Retornou {resultado}\n"


        print(f"{data_hora}: {func.__name__.upper()}")
        return resultado

# -------5 -Criando o Arquivo de Log chamado 'log.txt'.--com metodo with opem--------------------
def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# ----Escrevendo uma linha dentro do meu 'arquivo' ==>> "log.txt".
        arquivo.write(
                f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. "
                f"Retornou {resultado}\n"
            )
# ---- Essa funcao vai abrir o Arquivo "log.txt" e Escrever "data_hora" , Funcao nome" e "Retorno dos resultados"

        print(f"{data_hora}: {func.__name__.upper()}")
        return resultado

    return envelope