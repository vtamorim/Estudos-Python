import pygame
import sys
import random

pygame.init()


def atirar_principal():
    novo_tiro = tiro.get_rect(center=(jogador_x + jogador_width // 2, jogador_y))
    tiros_principal.append(novo_tiro)

def atirar_inimigo():
    inim_tiro = tiro.get_rect(center=(jogador_x + jogador_height // 2, 50))
    tiros_inimigo.append(inim_tiro)

def nada():
    return ''
width, height = 1200, 600
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("Modelo Básico de Jogo - Pygame")

PRETO = (0, 0, 0)
nave = pygame.transform.scale(pygame.image.load('nave.png'), (50, 50)) 
nave_rect = nave.get_rect(topleft= (100,100))
inimigo = pygame.transform.scale(pygame.image.load('qfoi.png'),(50,50))
# Jogador
jogador_width, jogador_height = 50, 50
jogador_x, jogador_y = width // 2, height - jogador_height - 10
velocidade = 0.5

# Tiro
tiro = pygame.transform.scale(pygame.image.load('bullet.png'), (5, 5))
tiros_principal = []
tiros_inimigo = []

fundo = pygame.transform.scale(pygame.image.load('eae.jpg'),(width,height)).convert_alpha()

# Clock
clock = pygame.time.Clock()
rodando = True

intervalo =  50
possibili = True

ultimo_gol = 0
ganhou = True
perdeu = True

jogador_vel_x = 0
jogador_vel_y = 0


inimigo_y = random.randint(-1,3)
inimigo_x = random.randint(0, width - height)
inimigo_vel_x = 0
inimigo_vel_y = 0


inimigo_rect = inimigo.get_rect(topleft=(width // 2, 100))

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    jogador_x += jogador_vel_x
    jogador_y += jogador_vel_y
    jogador_vel_x *= 0.9
    jogador_vel_y *= 0.9

    inimigo_x += inimigo_vel_x
    inimigo_y += inimigo_vel_y
    inimigo_vel_y *= 0.9
    inimigo_vel_x *= 0.9


    if inimigo_x <= 0 or inimigo_x + 50 >= width:
        inimigo_vel_x *= -1
    if inimigo_y <= 0 or inimigo_y + 50 >= height:
        inimigo_vel_y *= -1
        
    tempo_ =  pygame.time.get_ticks()

    teclas = pygame.key.get_pressed()
    if teclas: 
        if teclas[pygame.K_w]:
            jogador_vel_y -= velocidade
        if teclas[pygame.K_s]:
            jogador_vel_y += velocidade
        if teclas[pygame.K_a]:
            jogador_vel_x -= velocidade
        if teclas[pygame.K_d]:
            jogador_vel_x += velocidade
        if teclas[pygame.K_SPACE] and possibili:
            atirar_principal()
            ultimo_gol = pygame.time.get_ticks()
            possibili = False

    if not possibili and tempo_ - ultimo_gol >= intervalo:
        possibili= True


    if teclas:
        if teclas[pygame.K_SPACE] and possibili:
            atirar_inimigo()
        else:
            nada()
    

    
    for tiro_rect in tiros_principal[:]:
        tiro_rect.y -= 10
        if tiro_rect.y < 0:  
            tiros_principal.remove(tiro_rect)
        if tiro_rect.colliderect(inimigo_rect):
            ganhou = False
            tiros_principal.remove(tiro_rect)
    
    for inim_rect in tiros_inimigo[:]:
        inim_rect.y += 10
        if inim_rect.y > height:
            tiros_inimigo.remove(inim_rect)
        jogador_rect = pygame.Rect(jogador_x, jogador_y, jogador_width, jogador_height)
        if inim_rect.colliderect(jogador_rect):
            perdeu = False
            tiros_inimigo.remove(inim_rect)
           



    if rodando: 
        if jogador_y < 0:
            jogador_y = 0
        if jogador_y + jogador_height > height:
            jogador_y = height - jogador_height
        if jogador_x < 0:
            jogador_x = 0
        if jogador_x + jogador_width > width:
            jogador_x = width - jogador_width
    tela.blit(fundo,(0,0))
    tela.blit(nave, (jogador_x, jogador_y))
    tela.blit(inimigo, (jogador_x, jogador_y - jogador_y))
    if ganhou is not None or perdeu is not None:
        tela.fill(PRETO)
        if ganhou:
            tela.fill(PRETO)
        elif perdeu:
            tela.fill(PRETO)
        if teclas[pygame.K_r]:
            ganhou = None
            perdeu = None
            tiros_inimigo.clear()
            tiros_principal.clear()

    for inim_rect in tiros_inimigo:
        tela.blit(tiro, inim_rect)
    for tiro_rect in tiros_principal:
        tela.blit(tiro, tiro_rect)
    

    pygame.display.update()
    clock.tick(60)
'''
import pygame
import sys

pygame.init()


def atirar_principal():
    novo_tiro = tiro.get_rect(center=(jogador_x + jogador_width // 2, jogador_y))
    tiros_principal.append(novo_tiro)

def atirar_inimigo():
    inim_tiro = tiro.get_rect(center=(jogador_x + jogador_height // 2, 50))
    tiros_inimigo.append(inim_tiro)

def nada():
    return ''
width, height = 1200, 600
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("Modelo Básico de Jogo - Pygame")

PRETO = (0, 0, 0)
nave = pygame.transform.scale(pygame.image.load('nave.png'), (50, 50)) 
nave_rect = nave.get_rect(topleft= (100,100))
inimigo = pygame.transform.scale(pygame.image.load('qfoi.png'),(50,50))
# Jogador
jogador_width, jogador_height = 50, 50
jogador_x, jogador_y = width // 2, height - jogador_height - 10
velocidade = 0.5

# Tiro
tiro = pygame.transform.scale(pygame.image.load('bullet.png'), (5, 5))
tiros_principal = []
tiros_inimigo = []

fundo = pygame.transform.scale(pygame.image.load('eae.jpg'),(width,height)).convert_alpha()

# Clock
clock = pygame.time.Clock()
rodando = True

intervalo =  50
possibili = True

ultimo_gol = 0

jogador_vel_x = 0
jogador_vel_y = 0

# Definir um retângulo para o inimigo
inimigo_rect = inimigo.get_rect(topleft=(width // 2, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    jogador_x += jogador_vel_x
    jogador_y += jogador_vel_y
    jogador_vel_x *= 0.9
    jogador_vel_y *= 0.9

    tempo_ = pygame.time.get_ticks()

    teclas = pygame.key.get_pressed()
    if teclas: 
        if teclas[pygame.K_w]:
            jogador_vel_y -= velocidade
        if teclas[pygame.K_s]:
            jogador_vel_y += velocidade
        if teclas[pygame.K_a]:
            jogador_vel_x -= velocidade
        if teclas[pygame.K_d]:
            jogador_vel_x += velocidade
        if teclas[pygame.K_SPACE] and possibili:
            atirar_principal()
            ultimo_gol = pygame.time.get_ticks()
            possibili = False

    if not possibili and tempo_ - ultimo_gol >= intervalo:
        possibili = True

    if jogador_y < 0:
        jogador_y = 0
    if jogador_y + jogador_height > height:
        jogador_y = height - jogador_height
    if jogador_x < 0:
        jogador_x = 0
    if jogador_x + jogador_width > width:
        jogador_x = width - jogador_width
    
    for tiro_rect in tiros_principal[:]:
        tiro_rect.y -= 10
        if tiro_rect.y < 0:  
            tiros_principal.remove(tiro_rect)
        if tiro_rect.colliderect(inimigo_rect):
            rodando = False
            tiros_principal.remove(tiro_rect)
    
    for inim_rect in tiros_inimigo[:]:
        inim_rect.y += 10
        if inim_rect.y > height:
            tiros_inimigo.remove(inim_rect)
        jogador_rect = pygame.Rect(jogador_x, jogador_y, jogador_width, jogador_height)
        if inim_rect.colliderect(jogador_rect):
            rodando = False
            tiros_inimigo.remove(inim_rect)
    
    
    
    tela.blit(fundo, (0, 0))
    tela.blit(nave, (jogador_x, jogador_y))
    tela.blit(inimigo, inimigo_rect)

    for tiro_rect in tiros_principal:
        tela.blit(tiro, tiro_rect)
    for inim_rect in tiros_inimigo:
        tela.blit(tiro, inim_rect)

    pygame.display.update()
    clock.tick(60)

'''