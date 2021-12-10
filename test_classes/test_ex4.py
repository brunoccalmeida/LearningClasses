from Classes.Ex4 import Pessoa
from unittest import TestCase


class TestePessoa(TestCase):

    def teste_envelhercer(self):
        pessoa1 = Pessoa('João', 65, 88, 1.70)
        pessoa1.envelhecer(3)
        self.assertEqual(68, pessoa1.idade)
        self.assertEqual(1.70, pessoa1.altura)

        pessoa2 = Pessoa('Júlia', 6, 20, 1.35)
        pessoa2.envelhecer(6)
        self.assertEqual(12, pessoa2.idade)
        self.assertEqual(1.65, round(pessoa2.altura, 2))

        pessoa3 = Pessoa('Jana', 21, 55, 1.65)
        pessoa3.envelhecer(3)
        self.assertEqual(24, pessoa3.idade)
        self.assertEqual(1.65, round(pessoa3.altura, 2))

        pessoa4 = Pessoa('Helena', 19, 50, 1.70)
        pessoa4.envelhecer(5)
        self.assertEqual(24, pessoa4.idade)
        self.assertEqual(1.75, round(pessoa4.altura, 2))

    def teste_engordar(self):
        pessoa1 = Pessoa('João', 65, 88, 1.70)
        pessoa1.engordar(7)
        self.assertEqual(95, pessoa1.peso)

        pessoa2 = Pessoa('Lily', 65, 50, 1.70)
        pessoa2.engordar(22)
        self.assertEqual(72, pessoa2.peso)

    def teste_emagrecer(self):
        pessoa1 = Pessoa('João', 65, 88, 1.70)
        pessoa1.emagrecer(7)
        self.assertEqual(81, pessoa1.peso)

        pessoa2 = Pessoa('Lily', 65, 50, 1.70)
        pessoa2.emagrecer(3)
        self.assertEqual(47, pessoa2.peso)

    def teste_crescer(self):
        pessoa1 = Pessoa('João', 65, 88, 1.70)
        pessoa1.crescer(0.15)
        self.assertEqual(1.85, round(pessoa1.altura, 2))

        pessoa2 = Pessoa('Lily', 65, 50, 1.70)
        pessoa2.crescer(0.05)
        self.assertEqual(1.75, round(pessoa2.altura, 2))

