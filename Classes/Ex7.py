class Tamagoshi:
    def __init__(self, nome, fome, saude, idade):
        self.saude = saude
        self.fome = fome
        self.nome = nome
        self.idade = idade

    def alterar_nome(self, nome):
        self.nome = nome

    def alterar_fome(self, fome):
        if 0 <= fome <= 10:
            self.fome = fome

    def alterar_saude(self, saude):
        if 0 <= saude <= 10:
            self.saude = saude

    def alterar_idade(self, idade):
        if 1 <= idade <= 100:
            self.idade = idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def retornar_humor(self):
        return self.saude + self.fome

