import pygame
from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.gameimage import *
import dificuldade
import jogo
import ranking

class Menu:
    def __init__(self, width, height): # Inicialização do MENU
        self.janela = Window(width, height)
        self.janela.set_background_color((246, 255, 238))
        self.janela.set_title("Space Invaders")
        self.bg = GameImage("assets/sprites/menu/bg2.jpg")
        self.mouse = Window.get_mouse()
        self.reload_mouse = 2

        self.logo = Sprite("assets/sprites/menu/logo.png")
        self.logo.x = self.janela.width / 2 - self.logo.width / 2
        self.logo.y = 35

        self.buttons = [
            Button("assets/sprites/menu/botao-iniciar.png", 300, self.start_game, self.janela),
            Button("assets/sprites/menu/botao-dificuldade.png", 400, self.set_difficulty, self.janela),
            Button("assets/sprites/menu/botao-ranking.png", 500, self.show_ranking, self.janela),
            Button("assets/sprites/menu/botao-sair.png", 600, self.quit_game, self.janela)
        ]

    def start_game(self): # Ação
        jogo.start(self.janela, self.reload_mouse)

    def set_difficulty(self): # Ação
        dificuldade.start(self.janela, self.reload_mouse)

    def show_ranking(self): # Ação
        ranking.start(self.janela, self.reload_mouse)

    def quit_game(self): # Ação
        self.janela.close()

    def run(self): # Executar o MENU
        while True:
            self.bg.draw()
            self.logo.draw()
            for button in self.buttons:
                button.draw()
                if self.mouse.is_over_object(button.sprite) and self.mouse.is_button_pressed(1) and self.reload_mouse <= 0:
                    self.reload_mouse = 2
                    button.action()

            if self.reload_mouse > 0:
                self.reload_mouse -= 0.02

            self.janela.update()

class Button:
    def __init__(self, image_path, y, action, janela): # Inicializar os Botões
        self.sprite = Sprite(image_path)
        self.sprite.x = janela.width / 2 - self.sprite.width / 2
        self.sprite.y = y
        self.action = action

    def draw(self): # Desenhar os Botões
        self.sprite.draw()

if __name__ == "__main__":
    menu = Menu(1000, 800)
    menu.run()
