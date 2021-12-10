class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.altura = altura
        self.peso = peso
        self.idade = idade
        self.nome = nome

    def envelhecer(self, anos):
        for _ in range(anos):
            self.idade += 1
            if self.idade < 21:
                self.altura += 0.05

    def engordar(self, kg):
        self.peso = self.peso + kg

    def emagrecer(self, kg):
        self.peso = self.peso - kg

    def crescer(self, cm):
        self.altura = self.altura + cm

