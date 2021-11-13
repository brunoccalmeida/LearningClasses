from Ex5 import ContaCorrente
from unittest import TestCase


class TestContaCorrente(TestCase):

    def teste_alterar_nome(self):
        correntista1 = ContaCorrente(23044, 'Bruno', 54000)
        self.assertEqual('Bruno', correntista1.nome_correntista)
        correntista1.alterar_nome('Bruno Almeida')
        self.assertEqual('Bruno Almeida', correntista1.nome_correntista)

    def teste_deposito(self):
        correntista1 = ContaCorrente(23044, 'Bruno', 54000)
        self.assertEqual(54000, correntista1.saldo)
        correntista1.deposito(330)
        self.assertEqual(54330, correntista1.saldo)

    def teste_saque(self):
        correntista1 = ContaCorrente(23044, 'Bruno', 54000)
        correntista1.saque(53000)
        self.assertEqual(1000, correntista1.saldo)
        self.assertEqual('Saldo insuficiente.', correntista1.saque(2000))
        self.assertEqual(1000, correntista1.saldo)

        correntista2 = ContaCorrente(23034, 'Gina')
        self.assertEqual(0, correntista2.saldo)
        self.assertEqual('Saldo insuficiente.', correntista2.saque(2000))
        self.assertEqual(0, correntista2.saldo)
