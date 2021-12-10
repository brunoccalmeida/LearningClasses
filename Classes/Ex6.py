class Televisao:
    def __init__(self, canal=1, volume=0):
        self.volume = volume
        self.canal = canal

    def mostrar_canal(self):
        return self.canal

    def mudar_canal(self, canal):
        if 1 <= canal <= 99:
            self.canal = canal
        else:
            if canal < 1:
                self.canal = 1
            if canal > 99:
                self.canal = 99

    def aumenta_volume(self):
        if self.volume < 100:
            self.volume += 1


    def diminui_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            self.volume = 0




