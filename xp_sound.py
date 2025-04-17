#!/bin/python3 

import pygame
from sys import argv
from os import environ
from time import sleep

def brilho_fraco(screen, x=10, y=70, size=[200,200]):
    brilho = pygame.Surface((size[0], size[1]), pygame.SRCALPHA)
    #brilho.fill((110, 140, 250))
    pygame.draw.circle(brilho, (255,255,255,10), (size[0]/2, size[0]/2), 25)
    screen.blit(brilho, (x, y))

def brilho_na_tela(screen, x=10, y=70, size=[120,120]):
    brilho = pygame.Surface((size[0],size[1]), pygame.SRCALPHA)
    # brilho forte
    #brilho.fill((110, 140, 250))
    pygame.draw.circle(brilho, (255,255,255,110), (size[0]/2, size[0]/2), 25)
    pygame.draw.circle(brilho, (255,255,255,120), (size[0]/3, size[0]/3), 25)
    pygame.draw.circle(brilho, (255,255,255,168), (size[0]/4,size[0]/4), 25)
    pygame.draw.circle(brilho, (255,255,255,140), (20, 20), 25)
    
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
    print("-"*35, "\n", f"{escape:^2}", "usage xp_sound.py sound.mp3", "\n","-"*35 )


tocou = True
running = True
#screen = pygame.display.set_mode((400,400))
screen =  pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)   #400,400)) 
                                   #screen_width, screen_height))
                                   # pygame.FULLSCREEN)

def padding_blue(size: list[int, int])->pygame.Surface:
    surface_top = pygame.Surface((size[0],size[1] ))#screen_width,screen_height))
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
        
        brilho_fraco(screen)
        brilho_na_tela(screen)
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
