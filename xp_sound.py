#!/bin/python3 

import pygame
from sys import argv
from os import environ
from time import sleep

def brilho(screen, x=10, y=70, size=[200,200]):
    brilho = pygame.Surface((size[0], size[1]), pygame.SRCALPHA)
    transparency = 5
    for _ in range(420, 88, -1):
        pygame.draw.circle(brilho, (255,255,255, transparency), (300,300), _)
        transparency += 0.25

   #brilho.fill((110, 140, 250))
  """  pygame.draw.circle(brilho, (255,255,255,5), (300,300), 420)
    pygame.draw.circle(brilho, (255,255,255,6), (300,300), 415)
    pygame.draw.circle(brilho, (255,255,255,7), (300,300), 405)
    pygame.draw.circle(brilho, (255,255,255,8), (300-10,300-10), 395)
    pygame.draw.circle(brilho, (255,255,255,9), (300-10,300-10), 375)

    pygame.draw.circle(brilho, (255,255,255,10), (300,300-12), 363)
    pygame.draw.circle(brilho, (255,255,255,11), (300,300-13), 350)
    pygame.draw.circle(brilho, (255,255,255,12), (300,300-15), 345)
    pygame.draw.circle(brilho, (255,255,255,13), (300,300-17), 340)
    pygame.draw.circle(brilho, (255,255,255,14), (300,300-19), 335)
    pygame.draw.circle(brilho, (255,255,255,15), (300,300-21), 325)

    pygame.draw.circle(brilho, (255,255,255,16), (300,300-21), 315)
    pygame.draw.circle(brilho, (255,255,255,17), (300,300-22), 300)


    pygame.draw.circle(brilho, (255,255,255,28), (300,300-24), 260)
    pygame.draw.circle(brilho, (255,255,255,30), (300,300-26), 255)
    pygame.draw.circle(brilho, (255,255,255,35), (300, 300-28), 235)
    pygame.draw.circle(brilho, (255,255,255,42), (300, 300-29), 215)
    pygame.draw.circle(brilho, (255,255,255,43), (300, 300-30), 190)
    pygame.draw.circle(brilho, (255,255,255,44), (300, 300-30), 175)
    pygame.draw.circle(brilho, (255,255,255, 46), (300, 300-30), 165)
    pygame.draw.circle(brilho, (255,255,255, 48), (300, 300-32), 150)
    pygame.draw.circle(brilho, (255,255,255, 49), (300,300-32), 140)
    pygame.draw.circle(brilho, (255,255,255, 51), (300,300-35), 125)
"""
    screen.blit(brilho, (x, y))



def shadow_text(screen, fonte,texto="Welcome", x=190, y=190, colour=(255,255,255), size=22,backcol=(100,100,100)):
    fonte.set_italic(True)
    fonte.bold = True
    # ^ bruh  
    offset = 1 + ( size // 10)
    black_text = fonte.render(texto, True, backcol)
    screen.blit(black_text, (x+offset, y+offset )) 
    texto_ = fonte.render(texto, True, colour)
    screen.blit(texto_, (x, y))
    

environ['SDL_VIDEO_CENTERED'] = '1'

pygame.mixer.pre_init(44100, -16, 2, 2048)

pygame.init()
pygame.font.init()

fonte = pygame.font.SysFont("Arial", 48)

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

try:
    sound = pygame.mixer.Sound("/home/kali/.icewm/Windows XP Startup.mp3")
except:
    escape = ""
    print("-"*35, "\n", f"{escape:^2}", "startup audio not found! ", "\n","-"*35 )


tocou = True
running = True

screen =  pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

def padding_blue(size: list[int, int])->pygame.Surface:

    surface_top = pygame.Surface((size[0],size[1] ))
    surface_top.fill((20, 10, 250))

    pygame.draw.aaline(surface_top, (140, 180, 230), (0, size[1] -2), (size[0] / 8, size[1] -1), 20)
    # azul escuro # dividido por 8
    
    pygame.draw.aaline(surface_top, (180, 180, 200), (size[0] / 8, size[1] -1), (size[0] / 4, size[1] -1), 20)
    # cinza # dividido por 4
    pygame.draw.aaline(surface_top, (220, 220, 220), (size[0] / 4, size[1] -1), (size[0] / 2, size[1] -1), 20)
    # branco # dividido por 2
    pygame.draw.aaline(surface_top, (140, 180, 220), (size[0] / 2, size[1] -1), (size[0] / 1.333, size[1] -1), 20)
    # cinza # dividido por 1.33333333333333
    pygame.draw.aaline(surface_top, (110, 140, 250), (size[0] / 1.333, size[1] -1), (size[0] / 1.142, size[1] -1), 20)
    # AZUL ESCURO 
    pygame.draw.aaline(surface_top, (120, 120, 255), (size[0] / 1.142, size[1] -1), (size[0], size[1] -2), 20)
    # top line  

    pygame.draw.aaline(surface_top, (45,42,20), (0, 2), (size[0] / 16, 0), 40)
    pygame.draw.aaline(surface_top, (120,20,30), (size[0] / 16, 0), (size[0] / 14, 0), 40)
    pygame.draw.aaline(surface_top, (200, 40, 12), (size[0] / 14, 0), (size[0] / 12, 0), 40)
    pygame.draw.aaline(surface_top, (230, 82, 14), (size[0] /12, 0), (size[0] /6, 0), 40)
    pygame.draw.aaline(surface_top, (250, 80, 20), (size[0] /6, 0), (size[0] / 2, 0), 40)
    pygame.draw.aaline(surface_top, (220, 120, 20), (size[0]/2, 0), (size[0]/1.333, 0), 40)
    pygame.draw.aaline(surface_top, (60, 160, 200), (size[0] / 1.333, 0) ,(size[0] / 1.142, 0), 40)
    pygame.draw.aaline(surface_top, (110, 140, 180), (size[0] / 1.142, 0), (size[0], 2), 40)
    return surface_top

counter = 1


while running:

        pygame.time.delay(60)
        screen.fill((110, 140, 250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        brilho(screen, x=0,y=0,size=[screen_width/2, screen_height/1.3])
        
        surface_top = padding_blue([screen_width,150])
    
        screen.blit(surface_top, (0,-5))
        
        screen.blit(surface_top, (0,screen_height-145))

        if counter >= 60:
            sound.play()
            pygame.time.delay(3500)

            running = False

        shadow_text(screen, fonte, x=screen_width/2, y=screen_height/2)
        
        counter += 1
        
        pygame.display.update()

pygame.display.quit()
pygame.quit()
exit()
