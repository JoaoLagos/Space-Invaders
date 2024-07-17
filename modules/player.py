from PPlay.sprite import *

class Player(Sprite):
    def __init__(self, window, image="assets/sprites/jogo/nave.png"):
        super().__init__(image, 1)  # Chama o construtor da classe Sprite
        self.x = window.width / 2 - self.width / 2
        self.y = window.height - self.height - 10
        self.vida = 3
        self.rBullet = 0
        self.pontos = 0
        self.velx = 300

        #self.draw()