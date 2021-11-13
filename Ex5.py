class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.saldo = saldo
        self.nome_correntista = nome_correntista
        self.numero_conta = numero_conta

    def alterar_nome(self, nome):
        self.nome_correntista = nome

    def deposito(self, valor):
        self.saldo = self.saldo + valor

    def saque(self, valor):
        if valor > self.saldo:
            return f'Saldo insuficiente.'
        else:
            self.saldo = self.saldo - valor


