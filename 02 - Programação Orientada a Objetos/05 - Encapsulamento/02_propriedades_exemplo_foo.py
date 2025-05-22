
# --- Property() ou Propriedade ---.

# O 'property' serve para 'Criar Atributos' e Gerenciar as suas Classes. 
# De modo Que, Quando voce possa precisar Modificar a sua implementacao interna
#  do codigo sem Sem Auterar a API publica da Classe. 
# Exemplo Quando 'X = 10' ou 'x = 17', ou 'x = Nome' etc... 
# Para Usar o  'property' Utilizamos um Decorador Tipo '@' ==> @property. 
# o '@' decorador e uma funcao que executa antes da sua funcao.

class Foo:  # Aqui temos uma classe que Chamamos de Foo ou poderia ser Qualquer Nome.. 
    def __init__(self, x=None):
        self._x = x     # Aqui temos uma Variavel Privada.

    @property   # Aqui temos como Variar o Atributo 'X' disponivel na nossa Class.
    def x(self):
        return self._x or 0 # Aqui a Variavel pega o valor de 'X' ou retorna '0'.

    @x.setter   # Aqui vai "inferir" ou modificar o valor se self._x =>10 para self._x =20 
    def x(self, value):
        self._x += value

    # @x.setter   # Aqui nao autera ou  "inferir"  no processo so retorna o valor 10.
    # def x(self, value):
    #    return self._x + value




    # @x.setter   # Aqui voce pode "inferir" ou 'modificar' no processo de atribuicao do atributo.
    # def x(self, value): # O setter Vai receber 2 Valores o Objeto 'foo = 10' e o 'foo.x = 10'
    #    _x = self._x or 0
    #    _value = value or 0
    #    self._x = _x +_value


    # @x.deleter  # Aqui Temos o processo de delecao do atributo.
    # def x(self):
    #    self._x = 0

    @x.deleter  # Aqui Temos o processo de delecao do atributo.
    def x(self):
        # self._x = 0
        self._x = -1

  

print("------------------------")
foo = Foo(10)   # foo ==> vale 10
print(foo.x)    # >>> 10

foo.x = 10
print(foo.x)    # >>> -1

del foo.x
print(foo.x)    # >>> 9


print("-------------------------")
foo = Foo(10)   # foo ==> vale 10
print(foo.x)    # >>> 10

del foo.x
print(foo.x)    # >>> 20

foo.x = 10
print(foo.x)    # >>> -1

print("-------------------------")

foo = Foo(10)   # foo ==> vale 10
del foo.x
print(foo.x)    # >>> 10

foo.x = 10
print(foo.x)    # >>> -1

print("-------------------------")
