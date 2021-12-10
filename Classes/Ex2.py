class Quadrado:

    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def muda_valor_lado(self, valor_lado):
        self.tamanho_do_lado = valor_lado

    def retornar_valor_lado(self):
        return self.tamanho_do_lado

    def calcular_area(self):
        return int(self.tamanho_do_lado)**2


