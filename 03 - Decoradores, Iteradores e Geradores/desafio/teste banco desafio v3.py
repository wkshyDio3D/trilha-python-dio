

import json
from datetime import datetime
from abc import ABC, abstractmethod
import textwrap
import os

CAMINHO_DADOS = "dados.json"

# -------------------- Classes --------------------

class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "endereco": self.endereco,
            "contas": [conta.numero for conta in self.contas]
        }

    @staticmethod
    def from_dict(dados):
        return Cliente(dados["nome"], dados["cpf"], dados["endereco"])


class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.agencia = "0001"
        self.saldo = 0
        self.transacoes = []

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        self.transacoes.append(Saque(valor))
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False
        self.saldo += valor
        self.transacoes.append(Deposito(valor))
        return True

    def exibir_extrato(self):
        print(f"\nExtrato da conta {self.numero}:")
        if not self.transacoes:
            print("Sem movimentações.")
        else:
            for t in self.transacoes:
                print(f"{t.data} - {t.tipo}: R$ {t.valor:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")

    def to_dict(self):
        return {
            "numero": self.numero,
            "agencia": self.agencia,
            "saldo": self.saldo,
            "cliente_cpf": self.cliente.cpf,
            "transacoes": [t.to_dict() for t in self.transacoes]
        }

    @staticmethod
    def from_dict(dados, cliente, transacoes_dicts):
        conta = Conta(dados["numero"], cliente)
        conta.saldo = dados["saldo"]
        conta.transacoes = [Transacao.from_dict(t) for t in transacoes_dicts]
        return conta


class Transacao(ABC):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    @abstractmethod
    def tipo(self):
        pass

    def to_dict(self):
        return {
            "valor": self.valor,
            "data": self.data,
            "tipo": self.tipo
        }

    @staticmethod
    def from_dict(d):
        if d["tipo"] == "Saque":
            return Saque(d["valor"], d["data"])
        elif d["tipo"] == "Depósito":
            return Deposito(d["valor"], d["data"])


class Saque(Transacao):
    def __init__(self, valor, data=None):
        super().__init__(valor)
        if data:
            self.data = data

    @property
    def tipo(self):
        return "Saque"


class Deposito(Transacao):
    def __init__(self, valor, data=None):
        super().__init__(valor)
        if data:
            self.data = data

    @property
    def tipo(self):
        return "Depósito"

# -------------------- Banco --------------------

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def salvar_dados(self):
        dados = {
            "clientes": [c.to_dict() for c in self.clientes],
            "contas": [c.to_dict() for c in self.contas],
            "transacoes": [t for c in self.contas for t in c.transacoes]
        }
        with open(CAMINHO_DADOS, "w") as f:
            json.dump(dados, f, indent=4)

    def carregar_dados(self):
        if not os.path.exists(CAMINHO_DADOS):
            return

        with open(CAMINHO_DADOS, "r") as f:
            dados = json.load(f)

        cpf_para_cliente = {}
        for c_dict in dados["clientes"]:
            cliente = Cliente.from_dict(c_dict)
            cpf_para_cliente[cliente.cpf] = cliente
            self.clientes.append(cliente)

        for c_dict in dados["contas"]:
            cliente = cpf_para_cliente.get(c_dict["cliente_cpf"])
            transacoes = [t for t in dados["transacoes"] if t["valor"] in [tr["valor"] for tr in c_dict["transacoes"]]]
            conta = Conta.from_dict(c_dict, cliente, transacoes)
            cliente.adicionar_conta(conta)
            self.contas.append(conta)

    def criar_cliente(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        if any(c.cpf == cpf for c in self.clientes):
            print("CPF já cadastrado.")
            return
        cliente = Cliente(nome, cpf, endereco)
        self.clientes.append(cliente)
        print("Cliente criado com sucesso.")

    def criar_conta(self):
        cpf = input("Informe o CPF do cliente: ")
        cliente = next((c for c in self.clientes if c.cpf == cpf), None)
        if not cliente:
            print("Cliente não encontrado.")
            return
        numero = str(len(self.contas) + 1).zfill(4)
        conta = Conta(numero, cliente)
        cliente.adicionar_conta(conta)
        self.contas.append(conta)
        print(f"Conta {numero} criada com sucesso.")

    def acessar_conta(self):
        numero = input("Número da conta: ")
        conta = next((c for c in self.contas if c.numero == numero), None)
        if not conta:
            print("Conta não encontrada.")
            return

        while True:
            print("\n1 - Sacar\n2 - Depositar\n3 - Extrato\n0 - Voltar")
            op = input("Opção: ")
            if op == "1":
                valor = float(input("Valor do saque: "))
                conta.sacar(valor)
            elif op == "2":
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)
            elif op == "3":
                conta.exibir_extrato()
            elif op == "0":
                break
            else:
                print("Opção inválida.")

# -------------------- Execução --------------------

def main():
    banco = Banco()
    banco.carregar_dados()

    while True:
        print("\n==== Sistema Bancário ====")
        print("1 - Novo cliente")
        print("2 - Nova conta")
        print("3 - Acessar conta")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            banco.criar_cliente()
        elif opcao == "2":
            banco.criar_conta()
        elif opcao == "3":
            banco.acessar_conta()
        elif opcao == "0":
            banco.salvar_dados()
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
