import pygame
from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.gameimage import *
import dificuldade
import jogo
import ranking


# JANELA
janela_width = 1000
janela_height = 800
janela = Window(janela_width, janela_height)
janela.set_background_color(((246, 255, 238)))
bg = GameImage("assets/sprites/menu/bg2.jpg")

# ENTRADA
mouse = Window.get_mouse()
reloadMouse = 5

janela.set_title("Space Invaders")

# SPRITES
## Logo
logo = Sprite("assets/sprites/menu/logo.png")
logo.x = janela.width/2 - logo.width/2
logo.y = 35

# Botão Iniciar
botao_iniciar = Sprite("assets/sprites/menu/botao-iniciar.png")
botao_iniciar.x = janela.width/2 - botao_iniciar.width/2
botao_iniciar.y = 300

# Botão Dificuldade
botao_dificuldade = Sprite("assets/sprites/menu/botao-dificuldade.png")
botao_dificuldade.x = janela.width/2 - botao_dificuldade.width/2
botao_dificuldade.y = 400

# Botão Ranking
botao_ranking = Sprite("assets/sprites/menu/botao-ranking.png")
botao_ranking.x = janela.width/2 - botao_ranking.width/2
botao_ranking.y = 500

# Botão Sair
botao_sair = Sprite("assets/sprites/menu/botao-sair.png")
botao_sair.x = janela.width/2 - botao_sair.width/2
botao_sair.y = 600

while True:
    bg.draw()  

    if mouse.is_over_object(botao_iniciar) and mouse.is_button_pressed(1) and reloadMouse<=0:
        reloadMouse = 5
        jogo.start(janela, reloadMouse)

    if mouse.is_over_object(botao_dificuldade) and mouse.is_button_pressed(1) and reloadMouse<=0:
        reloadMouse = 5
        dificuldade.start(janela, reloadMouse)
        
        
    if mouse.is_over_object(botao_ranking) and mouse.is_button_pressed(1) and reloadMouse<=0:
        reloadMouse = 5
        ranking.start(janela, reloadMouse)    

    if mouse.is_over_object(botao_sair) and mouse.is_button_pressed(1) and reloadMouse<=0:
        janela.close()

    if reloadMouse > 0:
        reloadMouse -= 0.02

    logo.draw()
    botao_iniciar.draw() 
    botao_dificuldade.draw()
    botao_ranking.draw()
    botao_sair.draw()

    janela.update()
