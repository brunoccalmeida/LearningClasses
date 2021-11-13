from unittest import TestCase
from Ex2 import Quadrado


class TesteQuadrado(TestCase):

    def teste_muda_valor_lado(self):
        quadrado1 = Quadrado(4)
        quadrado1.muda_valor_lado(5)
        self.assertEqual(5, quadrado1.tamanho_do_lado)

    def teste_retorna_valor_lado(self):
        quadrado2 = Quadrado(3)
        self.assertEqual(3, quadrado2.retornar_valor_lado())

    def teste_calcular_area(self):
        quadrado3 = Quadrado(5)
        self.assertEqual(25, quadrado3.calcular_area())
