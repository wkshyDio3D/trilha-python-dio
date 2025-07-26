

from abc import ABC, abstractmethod
from datetime import datetime, timezone

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now(timezone.utc).strftime("%d-%m-%Y %H:%M:%S")
        })

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.depositar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self._saldo = 0
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("\n@@@ Valor inválido para saque. @@@")
            return False

        if valor > self._saldo:
            print("\n@@@ Saldo insuficiente. @@@")
            return False

        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("\n@@@ Valor inválido para depósito. @@@")
            return False

        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        return None
    return cliente.contas[0]

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado. @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        print("\n@@@ Cliente não possui conta. @@@")
        return

    cliente.realizar_transacao(conta, transacao)

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado. @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        print("\n@@@ Cliente não possui conta. @@@")
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado. @@@")
        return

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        print("\n@@@ Cliente não possui conta. @@@")
        return

    print("\n ================ EXTRATO ================")
    print("\n ===  Nome do Cliente===", Cliente)
    transacoes = conta.historico.transacoes

    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes:
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            data = transacao["data"]
            print(f"{data} | {tipo:<10} R$ {valor:.2f}")

    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("==========================================")

def main():
    clientes = []
    cliente = Cliente("João da Silva", "123")
    conta = Conta("0001", cliente)
    cliente.adicionar_conta(conta)
    clientes.append(cliente)

    while True:
        print("\n[1] Depositar\n[2] Sacar\n[3] Extrato\n[0] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            depositar(clientes)
        elif opcao == "2":
            sacar(clientes)
        elif opcao == "3":
            exibir_extrato(clientes)
        elif opcao == "0":
            break
        else:
            print("\n@@@ Opção inválida. @@@")

if __name__ == "__main__":
    main()
