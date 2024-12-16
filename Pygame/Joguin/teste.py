import pygame
import sys
import random

pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo Simples - Movimento Aleatório do Inimigo")

# Cores
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)

# Jogador
jogador_tamanho = 50
jogador_x = LARGURA // 2
jogador_y = ALTURA - jogador_tamanho - 10
jogador_vel = 5

# Inimigo
inimigo_tamanho = 50
inimigo_x = random.randint(0, LARGURA - inimigo_tamanho)
inimigo_y = random.randint(0,0)
inimigo_vel = 3
inimigo_direcao_x = random.choice([-2, 2])
inimigo_direcao_y = random.choice([0, 0])

# Clock
clock = pygame.time.Clock()

# Loop do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= jogador_vel
    if teclas[pygame.K_RIGHT] and jogador_x < LARGURA - jogador_tamanho:
        jogador_x += jogador_vel
    if teclas[pygame.K_UP] and jogador_y > 0:
        jogador_y -= jogador_vel
    if teclas[pygame.K_DOWN] and jogador_y < ALTURA - jogador_tamanho:
        jogador_y += jogador_vel

    # Movimento do inimigo
    inimigo_x += inimigo_vel * inimigo_direcao_x
    inimigo_y += inimigo_vel * inimigo_direcao_y

    # Alterar direção ao atingir bordas
    if inimigo_x <= 0 or inimigo_x + inimigo_tamanho >= LARGURA:
        inimigo_direcao_x *= -1
    if inimigo_y <= 0 or inimigo_y + inimigo_tamanho >= ALTURA:
        inimigo_direcao_y *= -1

    # Verificar colisão entre jogador e inimigo
    jogador_rect = pygame.Rect(jogador_x, jogador_y, jogador_tamanho, jogador_tamanho)
    inimigo_rect = pygame.Rect(inimigo_x, inimigo_y, inimigo_tamanho, inimigo_tamanho)
    if jogador_rect.colliderect(inimigo_rect):
        print("Você perdeu!")
        rodando = False

    # Desenhar na tela
    tela.fill(PRETO)
    pygame.draw.rect(tela, AZUL, jogador_rect)
    pygame.draw.rect(tela, VERMELHO, inimigo_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
