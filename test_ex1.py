from Ex1 import Bola
from unittest import TestCase


class TesteBola(TestCase):
    def teste_troca_cor(self):
        bola1 = Bola('amarelo', 33, 'isopor')
        bola1.troca_cor('Azul')
        self.assertEqual('Azul', bola1.cor)

    def teste_mostra_cor(self):
        bola2 = Bola('roxo', 22, 'plástico')
        bola2.troca_cor('verde')
        self.assertEqual('verde', bola2.mostra_cor())
