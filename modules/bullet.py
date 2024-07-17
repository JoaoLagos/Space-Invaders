from PPlay.sprite import *

class Bullet(Sprite):
    def __init__(self, window, vely=200, image="assets/sprites/jogo/bullet.png"):
        super().__init__(image, 1)  # Chama o construtor da classe Sprite
        self.window = window
        self.vely = vely
        self.x = window.width / 2 - self.width / 2
        self.y = window.height - self.height - 10

        #self.draw()