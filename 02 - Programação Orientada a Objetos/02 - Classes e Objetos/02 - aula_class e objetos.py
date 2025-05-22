
# -- Nosso primeiro Programa Orientado a objetos ------------

# Criar um Programa para Registrar as Vendas de bicicletas do Joao. Que informa : COR, MODELO, 
# ANO e VALOR da Venda. e o que ela faz, (para, buzinar e correr).

# criando uma Nova Classe ==>>  "class bicicleta"
# 1 => Primeiro =>>> definimos a classe.

class bicicleta: # Criando e definindo o nome da minha class .
    # Paremetros a ser inicializados na minha "def".
    # => cor, 
    # => modelo,
    # => ano, 
    # => valor.
    # def __init__(self): ==>> Self ou this ou este ==>> e Uma referencia direta do Objeto ou instancia.

    def __init__(self, cor, modelo, ano, valor, aro=18): # Aqui define o Metodo construtor da class e a 
                                                 # baixo os Atributos da Class.
        # pass ==>>Igual a um bloco vazio para teste.
        # Aqui Temos "Self" recebendo os Respectivos Valores a eles atribuidos.
        # ('self.cor' => recebe => 'cor').
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro  #  Modelo 5 ==>> Usando o "Join". inserindo novo atributo.
        self.marcha = 1

    # 3 => Terceiro =>>> definimos os metodos.
    # Agora vamos definir os metodos (para, buzinar e correr), que sao parecidos com funcoes "def".
    def buzinar (self):
        print("Plim Plim ...")

    def parar(self):
        print("Parando a Bicicleta ...")
        print("Bicicleta Parada!")

    def correr(self):
        print(" Vrummmmmmm.....")

    def trocar_marcha(self):
        print(" Trocando Marcha ")

        if self.marcha >= 0 and self.marcha <= 8:
            print("A Marcha Atual E ==>> : ", self.marcha, " Baixa ")

        elif self.marcha >= 9 and self.marcha <= 16:
            print("A Marcha Atual E ==>> : ", self.marcha, " Media " )

        elif self.marcha >= 17 and self.marcha <= 25:
            print("A Marcha Atual E ==>> : ", self.marcha, " Alta " )

        else:
            print("Fora das opções")
        #    else:
         #       print(" nao foi Possivel Trocar de Marcha ... ")


    # def trocar_marcha(self, nro_marcha):
       # print(" Trocando Marcha ")

        # def _trocar_marcha():
        #    if nro_marcha > self.marcha:
        #        print("Marcha trocada ... ")

        #   else:
         #       print(" nao foi Possivel Trocar de Marcha ... ")

    # 6.1 criando o Metodo "__str__".
    # def __str__(self): # Resultado do "return f" no Print (b2).
        # return f""  # Aqui podemos colocar qualquer String.
             # "nome da class" : e os valores dos atributos.
        # # Modelo 1     
        # return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
        # Ou dessa forma abaixo para ficar mais bonito.
        # # Modelo 2
        # return f"Bicicleta: cor= {self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
        #pass

    # outra forma automatizada de ver nossos atributos.
    def __str__(self):
        # Modelo 3
        # return f"{self.__class__.__name__}"

        #  Modelo 4
        # return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"
    
        #  Modelo 5 ==>> Usando o "Join".
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        # Agora com esses atributos posso ir la nos atributos e inserir novos atributos a minha 
        # ==>> class Bicicleta: ==>> "self.aro = aro" que sera exibido automaticamente.
        # pass

# 2 => Segundo =>>> definimos as instancias 
# instanciando a  Bicicleta
# caloi = bicicleta("vermelha", "caloi", 2025, 600)
b1 = bicicleta("vermelha", "caloi", 2025, 1600)

# 4 => Quarto =>>> Agora Conseguimos executar o programa.
b1.buzinar()
b1.correr()
bicicleta.buzinar(b1)
b1.parar()
b1.trocar_marcha()

# b1.trocar_marcha()

# 5 => Quinto =>>> Quinto Agora tambem podemos pedir para exibir os atributos. 
print(b1.cor, b1.modelo, b1.ano, b1.valor)

# -----------------------------------
b2 = bicicleta("verde", "monark", 2000, 2300)
bicicleta.buzinar(b2)
print(b2.cor, b2.modelo)

b2.buzinar() # E o mesmo que ==>> bicicleta.buzinar(b2)


# 6 => Sexto =>>> Agora podemos voltar na "class" e criar ou definir um novo metodo "def" para 
# exibir as nossas instacias, para exibir quais sao os objetos e valores. de forma mais legivel 
# para o Usuario , usamos o metodo "str" que e ==>> "__str___".

# print(b2) # Modelo 1
# >>> Bicicleta: verde, monark, 2000, 2300

# print(b2) # Modelo 2
# >>> Bicicleta: cor= verde, modelo=monark, ano=2000, valor=2300

# print(b2) # # Modelo 3
# >>> bicicleta

# print(b2) # # Modelo 4
# >>> bicicleta: ['cor=verde', 'modelo=monark', 'ano=2000', 'valor=2300']

# print(b2) # # Modelo 5 ==>> usando o "join".
# >>> bicicleta: cor=verde, modelo=monark, ano=2000, valor=2300

print(b2) # # Modelo 5 ==>> usando o "join". Inserindo Novo atributo "aro=18"
# >>> bicicleta: cor=verde, modelo=monark, ano=2000, valor=2300, aro=18

b1.trocar_marcha()
# b2.trocar_marcha()