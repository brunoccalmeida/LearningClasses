from Classes.Ex7 import Tamagoshi
from unittest import TestCase


class TestTamagoshi(TestCase):
    def testa_alterar_nome(self):
        tamagoshi1 = Tamagoshi('Bichinho1', 10, 10, 1)
        self.assertEqual('Bichinho1', tamagoshi1.nome)
        tamagoshi1.alterar_nome('Bichinho10')
        self.assertEqual('Bichinho10', tamagoshi1.nome)

    def testa_alterar_fome(self):
        tamagoshi1 = Tamagoshi('Bichinho1', 10, 10, 1)
        self.assertEqual(10, tamagoshi1.fome)
        tamagoshi1.alterar_fome(9)
        self.assertEqual(9, tamagoshi1.fome)
        tamagoshi1.alterar_fome(11)
        self.assertEqual(9, tamagoshi1.fome)
        tamagoshi1.alterar_fome(-15)
        self.assertEqual(9, tamagoshi1.fome)

    def testa_alterar_saude(self):
        tamagoshi1 = Tamagoshi('Bichinho1', 10, 10, 1)
        self.assertEqual(10, tamagoshi1.saude)
        tamagoshi1.alterar_saude(5)
        self.assertEqual(5, tamagoshi1.saude)
        tamagoshi1.alterar_saude(12)
        self.assertEqual(5, tamagoshi1.saude)
        tamagoshi1.alterar_saude(-1)
        self.assertEqual(5, tamagoshi1.saude)

    def testa_alterar_idade(self):
        tamagoshi1 = Tamagoshi('Bichinho1', 10, 10, 1)
        self.assertEqual(1, tamagoshi1.idade)
        tamagoshi1.alterar_idade(2)
        self.assertEqual(2, tamagoshi1.idade)
        tamagoshi1.alterar_idade(99)
        self.assertEqual(99, tamagoshi1.idade)
        tamagoshi1.alterar_idade(112)
        self.assertEqual(99, tamagoshi1.idade)
        tamagoshi1.alterar_idade(-1)
        self.assertEqual(99, tamagoshi1.idade)

    def testa_retornar_humor(self):
        tamagoshi1 = Tamagoshi('Bichinho1', 10, 10, 1)
        self.assertEqual(20, tamagoshi1.retornar_humor())
        tamagoshi1.alterar_fome(5)
        self.assertEqual(15, tamagoshi1.retornar_humor())
        tamagoshi1.alterar_fome(-1)
        self.assertEqual(15, tamagoshi1.retornar_humor())
        tamagoshi1.alterar_fome(22)
        self.assertEqual(15, tamagoshi1.retornar_humor())
