

class Animal:
    def __init__(self, nro_patas):  # Construtor Pai
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)  # Chamando o construtor Pai

class FalarMixin:
    def falar(self):
        return(" Oiii Estou Falasndo ok ")
        print(" Oiii Estou Falasndo ok ")


class gato(Mamifero, FalarMixin):
    def __init__(self, cor_pelo, **kw):
        super().__init__(cor_pelo, **kw)

        # print(gato.mro())    # Aqui Temos dois Formas  para visualizar Qual e a ordem da resolucao dos metodos e  atributos.
        # print(gato.__mro__)
    pass



gato = gato(nro_patas=4, cor_pelo="Preto")
print(gato)

print(gato.falar())
