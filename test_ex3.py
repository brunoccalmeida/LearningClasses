from unittest import TestCase
from Ex3 import Retangulo


class TesteRetangulo(TestCase):

    def teste_mudar_lados(self):
        retangulo1 = Retangulo(3, 4)
        retangulo1.mudar_valor_lados(2, 5)
        self.assertEqual((2, 5), (retangulo1.base, retangulo1.altura))

    def teste_retornar_lados(self):
        retangulo2 = Retangulo(6, 7)
        retangulo2.mudar_valor_lados(3, 8)
        self.assertEqual((3, 8), retangulo2.retornar_valor_lados())

    def teste_calcular_area(self):
        retangulo3 = Retangulo(4, 5)
        self.assertEqual(20, retangulo3.calcular_area())

    def teste_calcular_perimetro(self):
        retangulo4 = Retangulo(4,7)
        self.assertEqual(22, retangulo4.calcular_perimetro())
