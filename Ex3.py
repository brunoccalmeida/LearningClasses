class Retangulo:
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base

    def mudar_valor_lados(self, base, altura):
        self.base = base
        self.altura = altura

    def retornar_valor_lados(self):
        return self.base, self.altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (2 * self.base) + (2 * self.altura)

