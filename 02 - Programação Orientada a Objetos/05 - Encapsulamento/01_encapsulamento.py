
# ------------ Encapsulamento ---ou Protecao de Acesso ----------

#  Encapsulamento e agrupar dados e metodos que manipulam esses Dados em uma unica Unidade.
#  Isso impoe restricoes ao acesso diretoa variaveis e metodos evitando assim a modificacao
#  acidental de dados, a variavel de um objeto encapsulado so podera ser alterada
#  pelo metodo desse objeto. 


class Conta:
    # O Atributo "Saldo" esta como Privado Indicado por '_underline' ==> "_saldo". Nao pode ser auterado Diretamente.
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo     
        self.nro_agencia = nro_agencia
        

    # O valor do "_Saldo -> privado" sera auterado pelo Metodo "depositar que e -> publico"
    def depositar(self, valor):
        # ...
        self._saldo += valor

    # O valor do "_Saldo -> privado" sera auterado pelo Metodo "sacar que e -> publico"
    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(200)
print(conta.nro_agencia)
# print("Conta N' ", conta.nro_agencia)
print(conta.mostrar_saldo())
# print("R$", conta.mostrar_saldo(), "00")
