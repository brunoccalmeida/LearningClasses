from unittest import TestCase
from Ex6 import Televisao


class TestaTelevisao(TestCase):

    def testa_mostrar_canal(self):
        televisao1 = Televisao()
        televisao1.mudar_canal(5)
        self.assertEqual(5, televisao1.canal)
        televisao1.mudar_canal(12)
        self.assertEqual(12, televisao1.canal)

    def testa_mudar_canal(self):
        televisao1 = Televisao()
        televisao1.mudar_canal(22)
        self.assertEqual(22, televisao1.canal)
        televisao1.mudar_canal(122)
        self.assertEqual(99, televisao1.canal)
        televisao1.mudar_canal(0)
        self.assertEqual(1, televisao1.canal)
        televisao1.mudar_canal(999)
        self.assertEqual(99, televisao1.canal)

    def testa_aumentar_volume(self):
        televisao1 = Televisao(volume=97)
        televisao1.aumenta_volume()
        self.assertEqual(98, televisao1.volume)
        televisao1.aumenta_volume()
        self.assertEqual(99, televisao1.volume)
        televisao1.aumenta_volume()
        self.assertEqual(100, televisao1.volume)
        televisao1.aumenta_volume()
        self.assertEqual(100, televisao1.volume)

    def testa_diminuir_volume(self):
        televisao1 = Televisao(volume=3)
        televisao1.diminui_volume()
        self.assertEqual(2, televisao1.volume)
        televisao1.diminui_volume()
        self.assertEqual(1, televisao1.volume)
        televisao1.diminui_volume()
        self.assertEqual(0, televisao1.volume)
        televisao1.diminui_volume()
        self.assertEqual(0, televisao1.volume)