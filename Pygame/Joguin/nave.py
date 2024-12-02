import pygame
import sys

pygame.init()


def atirar_principal():
    novo_tiro = tiro.get_rect(center=(jogador_x + jogador_largura // 2, jogador_y))
    tiros_principal.append(novo_tiro)

def atirar_inimigo():
    inim_tiro = tiro.get_rect(center=(jogador_x + jogador_altura // 2, jogador_y))
    tiros_inimigo.append(inim_tiro)
LARGURA, ALTURA = 1200, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Modelo Básico de Jogo - Pygame")

PRETO = (0, 0, 0)
nave = pygame.transform.scale(pygame.image.load('nave.png'), (50, 50)) 
inimigo = pygame.transform.scale(pygame.image.load('OIP.jfif'),(50,50))
# Jogador
jogador_largura, jogador_altura = 50, 50
jogador_x, jogador_y = LARGURA // 2, ALTURA - jogador_altura - 10
velocidade = 0.5

# Tiro
tiro = pygame.transform.scale(pygame.image.load('bullet.png'), (5, 5))
tiros_principal = []
tiros_inimigo = []

fundo = pygame.transform.scale(pygame.image.load('R.png'),(LARGURA,ALTURA)).convert_alpha()

# Clock
clock = pygame.time.Clock()
rodando = True

jogador_vel_x = 0
jogador_vel_y = 0

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    jogador_x += jogador_vel_x
    jogador_y += jogador_vel_y
    jogador_vel_x *= 0.9
    jogador_vel_y *= 0.9

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        jogador_vel_y -= velocidade
    if teclas[pygame.K_s]:
        jogador_vel_y += velocidade
    if teclas[pygame.K_a]:
        jogador_vel_x -= velocidade
    if teclas[pygame.K_d]:
        jogador_vel_x += velocidade
    if teclas[pygame.K_SPACE]:
        atirar_principal()


    for tiro_rect in tiros_principal[:]:
        tiro_rect.y -= 10 
        if tiro_rect.y < 0:  
            tiros_principal.remove(tiro_rect)

    for inim_rect in tiros_inimigo[:]:
        tiro_rect.y += 10
        if tiro_rect.y > ALTURA:
            tiros_inimigo.remove(tiro_rect)

    if jogador_y < 0:
        jogador_y = 0
    if jogador_y + jogador_altura > ALTURA:
        jogador_y = ALTURA - jogador_altura
    if jogador_x < 0:
        jogador_x = 0
    if jogador_x + jogador_largura > LARGURA:
        jogador_x = LARGURA - jogador_largura


    tela.blit(fundo,(0,0))
    tela.blit(nave, (jogador_x, jogador_y))

    

    for tiro_rect in tiros_inimigo:
        tela.blit(tiro, inim_rect)
    for tiro_rect in tiros_principal:
        tela.blit(tiro, tiro_rect)

    pygame.display.update()
    clock.tick(60)
