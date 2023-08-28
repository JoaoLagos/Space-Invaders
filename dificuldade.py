import pygame
from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.gameimage import *

def start(janela, reloadMouse):
    mouse = Window.get_mouse()

    bg = GameImage("assets/sprites/menu/bg2.jpg")

    # SPRITES
    ## Dificuldade
    dificuldade = Sprite("assets/sprites/menu/botao-dificuldade.png")
    dificuldade.x = janela.width/2 - dificuldade.width/2
    dificuldade.y = 50
    dificuldade.draw()

    ## Fácil
    facil = Sprite("assets/sprites/dificuldade/dificuldade-facil.png")
    facil.x = janela.width/2 - facil.width/2
    facil.y = 300
    facil.draw()

    ## Médio
    medio = Sprite("assets/sprites/dificuldade/dificuldade-medio.png")
    medio.x = janela.width/2 - medio.width/2
    medio.y = 400
    medio.draw()

    ## Difícil
    dificil = Sprite("assets/sprites/dificuldade/dificuldade-dificil.png")
    dificil.x = janela.width/2 - dificil.width/2
    dificil.y = 500
    dificil.draw()
    while True:
        bg.draw()

        # FÁCIL
        if mouse.is_over_object(facil) and mouse.is_button_pressed(1) and reloadMouse<=0:
            #nivel = 1
            janela.clear()
            #return 1
            break

        #MÉDIO
        if mouse.is_over_object(medio) and mouse.is_button_pressed(1) and reloadMouse<=0: 
            #nivel = 2
            janela.clear()
            #return 2
            break
           
        # DIFÍCIL
        if mouse.is_over_object(dificil) and mouse.is_button_pressed(1) and reloadMouse<=0:
            #nivel = 3
            janela.clear()
            #return 3
            break
        
        if reloadMouse > 0:
            reloadMouse -= 0.02

        janela.draw_text(f"AINDA FALTA SER IMPLEMENTADO!!!", x=350, y=200, bold=True, size=18, color=(255,0,0))

        dificuldade.draw()
        facil.draw()
        medio.draw()
        dificil.draw()
        janela.update()