from PPlay.sprite import *

class Enemy(Sprite):  
    velx = 200  # Variável de classe para velocidade horizontal
    vely = 50  # Variável de classe para velocidade vertical
    rBullet = 0
    LBullets = []

    def __init__(self, window, image="assets/sprites/jogo/inimigo.png"):
        super().__init__(image, 1)  # Chama o construtor da classe Sprite
        self.window = window

    def move_horizontal(self):
        # Movimento Inimigo Horizontal EIXO X
        self.x += Enemy.velx*self.window.delta_time() #* (1 + (level-1)/2)
    
    def check_down(self):
        posFuturaX = self.x + Enemy.velx*self.window.delta_time() #* (1 + (level-1)/2)
        posFuturaY = self.y + Enemy.velx*self.window.delta_time()
        if posFuturaX <= 0:
            Enemy.velx = abs(Enemy.velx)
            return True
        if posFuturaX >= self.window.width-self.width:
            Enemy.velx = -Enemy.velx
            return True
        return False

    def move_vertical(self):
        # Movimento Inimigo Vertical EIXO Y
        self.y += Enemy.vely
