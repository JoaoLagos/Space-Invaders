from PPlay.sprite import *
from modules.bullet import *

class Player(Sprite):
    def __init__(self, window, teclado, image="assets/sprites/jogo/nave.png"):
        super().__init__(image, 1)  # Chama o construtor da classe Sprite
        self.window = window
        self.teclado = teclado
        self.x = window.width / 2 - self.width / 2
        self.y = window.height - self.height - 10
        self.vida = 3
        self.rBullet = 0
        self.pontos = 0
        self.velx = 300
        self.Lbullets = []

        #self.draw()

    def process_moviment(self):
        if self.teclado.key_pressed("A") and self.x >= 0:
            self.x -= self.velx*self.window.delta_time()
        if self.teclado.key_pressed("D") and self.x <= self.window.width-self.width:
                self.x += self.velx*self.window.delta_time()

    def process_bullet(self):
        if self.teclado.key_pressed("SPACE") and self.rBullet <= 0:
            self.rBullet = 10
            bullet = Bullet(self.window)
            bullet.x = self.x + self.width/2 - 3
            bullet.y = self.y
            self.Lbullets.append(bullet)

    def process_points(self, decaimentoPontos):
        self.pontos += int((100/decaimentoPontos)//1) #Incrementa pontos