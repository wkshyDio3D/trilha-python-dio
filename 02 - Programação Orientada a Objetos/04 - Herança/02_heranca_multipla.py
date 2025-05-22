
# -------- Heranca Multipla ------------

# Sintaxe da Heranca Multipla
# Quando uma Class filha herda de Varias Classes Pai, ela e chamade de Heranca Multipla.

# Exemplo ==>> Sintaxe da Heranca Multipla.
class a:    # Classe "a", e a classe => Pai.
    print(" Classe Pai - A")
    pass
class b:    # Classe "a", e a classe => Mae.
    print(" Classe Mae - B")
    pass

class c(a, b): # Aqui a Classe "c" ou "Classe filha" Herda da classe "a" e "b" ou "classe Mae" e "classe Pai".
    print(" Classe Filha - C -->> Herda da classe 'a' e 'b' ")
    pass

class d(a, b): # Aqui a Classe "d" ou "Classe filho" Herda da classe "a" e "b" ou "classe Pai" e "classe Mae".
    print(" Classe Filho - d -->> Herda da classe 'a' e 'b'' ")
    pass
# Fim Exemplo ==>> Sintaxe da Heranca Multipla.


print(" ")
# --------------------Heranca Multipla---------------------------
class Animal:     # Construtor pai ou Mae -"Animal".
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal): # Aqui o Contrutor filho "Mamifero" - Chamando o construtor Pai "Animal".
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)  


class Ave(Animal):  # Aqui o Contrutor filha "Ave" - Chamando o construtor Pai "Animal".
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)  


class Gato(Mamifero):   # Aqui o Contrutor neto "gato" - Chamando o construtor filho "Mamifero".
    pass


class Ornitorrinco(Mamifero, Ave):   # Aqui o Contrutor Neto "Ornitorrinco" - Chamando os construtores filho "Mamifero". e filha "Ave"
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)


ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
