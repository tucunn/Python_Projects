from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agencia: {self.agencia} '
              f'Conta: {self.conta} '
              f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass



class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print(f'Saldo insuficiente.')
            return

        self.saldo -= valor
        self.detalhes()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print(f'Saldo insuficiente.')
            return

        self.saldo -= valor
        self.detalhes()