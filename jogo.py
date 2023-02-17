from PPlay.gameimage import *
import pygame
from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.keyboard import *
import random
import ranking

''' Cria a matriz de inimigos '''
def cria_inimigos():
    Lista_inimigos = []
    for linha in range(5):
        lista_linha = []
        for coluna in range(6):
            inimigos = Sprite("assets/sprites/jogo/inimigo.png", 1)
            inimigos.x = (3*inimigos.width/2)*coluna + 1
            inimigos.y = (3*inimigos.height/2)*linha
            lista_linha.append(inimigos)
        Lista_inimigos.append(lista_linha)

    return Lista_inimigos

''' Faz o efeito piscante no Sprite '''
def efeito_piscante(sprite, cowdownInv):
    if 5<=cowdownInv<=10 or 15<=cowdownInv<=20 or 25<=cowdownInv<=30 or 35<=cowdownInv<=40: # Gambiarra
        sprite.hide()
    else: 
        sprite.unhide()

''' Inicializa essa janela '''
def start():
    # JANELA
    janela_width = 1000
    janela_height = 800
    janela = Window(janela_width, janela_height)
    # Background
    bg = GameImage("assets/sprites/jogo/bg2.jpg")

    # SPRITES
    ## Nave
    nave = Sprite("assets/sprites/jogo/nave.png", 1)
    nave.x = janela.width/2 - nave.width/2
    nave.y = janela.height - nave.height - 10
    nave.draw()

    ## Vidas
    Lvida = ["assets/sprites/jogo/vida1.png", "assets/sprites/jogo/vida2.png", "assets/sprites/jogo/vida3.png"]
    vida = Sprite(Lvida[-1], 1)
    vida.x = 5
    vida.y = 10

    teclado = Window.get_keyboard()

    # Listas
    Lbullets_Player = []
    Lbullets_Inimigo = []
    Linimigos = []
    Linimigos = cria_inimigos()

    # Contadores
    rBullet_Player = 0
    rBullet_Inimigo = 0
    # Variáveis
    level = 1
    velx_inimigo = 200 
    vely_inimigo = 100
    movimentoDescida = 0
    tempo = 0
    fps = 0
    frames = 0
    pontos = 0
    decaimentoPontos = 0 #Fator de divisão que aumenta com o passar do tempo, e reseta ao atingir um inimigo
    invensivel = 0
    gameOver = 0
    verificador_de_break = False

    while True:
        bg.draw()
        # NAVE
        # Movimento Nave
        velx_nave = 300
        if teclado.key_pressed("A") and nave.x >= 0:
            nave.x -= velx_nave*janela.delta_time()
        if teclado.key_pressed("D") and nave.x <= janela.width-nave.width:
                nave.x += velx_nave*janela.delta_time()

        # INIMIGOS
        for linha in Linimigos:
            for inimigo in linha:
                # Movimento Inimigo
                ## Movimento Horizontal EIXO X
                inimigo.x += velx_inimigo*janela.delta_time() * (1 + (level-1)/2)
                posFuturaX = inimigo.x + velx_inimigo*janela.delta_time() * (1 + (level-1)/2)
                posFuturaY = inimigo.y + vely_inimigo*janela.delta_time()
                if posFuturaX <= 0:
                    velx_inimigo = abs(velx_inimigo)
                    movimentoDescida = 1
                if posFuturaX >= janela_width-inimigo.width:
                    velx_inimigo = -velx_inimigo
                    movimentoDescida = 1
                ## Movimento Descida EIXO Y
                if movimentoDescida == 1:
                    for linha in Linimigos:
                        for inimigo in linha:
                            inimigo.y += 40
                    movimentoDescida = 0
                # GameOver caso inimigos atinjam a altura da nave
                if inimigo.y+inimigo.height >= nave.y:
                    janela.clear()
                    gameOver = 1
                    

                inimigo.draw()

        # BULLET
        ## Bullet Protagonista
        ### Bullet saindo da Nave
        if teclado.key_pressed("SPACE") and rBullet_Player <= 0:
            rBullet_Player = 10
            bullet = Sprite("assets/sprites/jogo/bullet.png", 1)
            bullet.x = nave.x + nave.width/2 - 3
            bullet.y = nave.y
            Lbullets_Player.append(bullet)

        ### Movimento Bullet
        vely_bulletAliado = 200 + 200*(level-1)/2
        for bullet in Lbullets_Player:
            bullet.y -= vely_bulletAliado*janela.delta_time()

            #### Colisão Inimigo e Bullet
            if len(Linimigos)>0 and (bullet.y <= Linimigos[-1][-1].y+Linimigos[-1][-1].height) and (bullet.y >= Linimigos[0][0].y):
                for linha in Linimigos:
                    for inimigo in linha:
                        if bullet.collided(inimigo):
                            Lbullets_Player.remove(bullet) 
                            linha.remove(inimigo)
                            pontos += int((100/decaimentoPontos)//1) #Incrementa pontos
                            decaimentoPontos = 1 #Reseta o fator decaimentoPontos
                            
                            if len(linha)==0:
                                Linimigos.remove(linha)

                            verificador_de_break = True # Para conseguir dar break em dois laços ao mesmo tempo ## Isso é necessário pois na hora de remover o bullet, ele fazia dnv caso encostasse em mais de um inimigo e ai crashava.
                            break

                    if verificador_de_break == True:
                        verificador_de_break = False
                        break

            #### Remove caso passe da tela
            elif bullet.y <= 0 - bullet.height:
                Lbullets_Player.remove(bullet)
            bullet.draw()

        ### Recarga do Bullet
        if rBullet_Player > 0:
            rBullet_Player -= 10*(1 + (level-1)/2) * janela.delta_time()

        ## Bullet Inimigo
        ### Bullet saindo dos inimigos
        if rBullet_Inimigo<=0:
            if len(Linimigos)>0: # Pois para sair o tiro do inimigo, precisa ter pelo menos um inimigo vivo para que ele possa atirar
                bullet = Sprite("assets/sprites/jogo/bullet.png", 1) # Tiro saindo de inimigo aleatório
                linhaInimigo = random.randint(0, len(Linimigos)-1)
                posInimigo = random.randint(0, len(Linimigos[linhaInimigo])-1)
                bullet.x = Linimigos[linhaInimigo][posInimigo].x + Linimigos[linhaInimigo][posInimigo].width/2
                bullet.y = Linimigos[linhaInimigo][posInimigo].y + Linimigos[linhaInimigo][posInimigo].height/2
                Lbullets_Inimigo.append(bullet)

                rBullet_Inimigo = random.randint(0, 16)/level # Recarregamento Bullet Inimigo (Aleatório)
        ### Movimento Bullet Inimigo
        for bullet in Lbullets_Inimigo:
            vely_bulletInimigo = 200*level
            bullet.y += vely_bulletInimigo*janela.delta_time()
            #### Remove caso passe da tela
            if bullet.y > janela.height:
                Lbullets_Inimigo.remove(bullet)
            #### Colisão Bullet com Player
            if invensivel <= 0: # Para validar a colisão, caso não tenha sido atingido recentemente
                if bullet.collided(nave):
                    Lbullets_Inimigo.remove(bullet)
                    Lvida.remove(Lvida[-1])
                    nave.x = janela.width/2 - nave.width/2
                    nave.y = janela.height - nave.height - 10
                    invensivel = 40 # Deixar invensível por um tempo, contagem mais abaixo
                    if len(Lvida)!=0:
                        vida = Sprite(Lvida[-1], 1)
                        vida.x = 5
                        vida.y = 10
            bullet.draw()
        
        if invensivel > 0: # Efeito Piscante 
            invensivel -= 25*janela.delta_time()
            efeito_piscante(nave, invensivel)
        
        ### Recarga Bullet Inimigo
        if rBullet_Inimigo>0:
            rBullet_Inimigo -= 10 * janela.delta_time()

        # FPS
        tempo += janela.delta_time()
        frames += 1
        if tempo >= 1:
            fps = frames
            frames = 0
            tempo = 0
        janela.draw_text(f"FPS: {fps}", x=janela.width-100,
                        y=0, color=(123, 20, 10), bold=True, size=16)
        janela.draw_text(f"Pontos: {pontos}", x=10,
                        y=vida.y + vida.height + 10, color=(255, 255, 255), bold=True, size=16)


        decaimentoPontos += janela.delta_time() # Incrementa no decaimentoPontos com o passar do tempo
        
        # Próxima Fase
        if len(Linimigos)==0:
            Lbullets_Player = []
            Lbullets_Inimigo = []
            Linimigos = cria_inimigos()
            if level<=2:
                level += 0.4
        
        # VOLTAR AO MENU 
        if teclado.key_pressed("ESC"):
            break
        if len(Lvida)==0 or gameOver==1:
            janela.clear()
            ranking.savePoints(pontos)
            break

        nave.draw()
        vida.draw()
        janela.update()
