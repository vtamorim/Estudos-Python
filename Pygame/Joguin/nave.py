import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Modelo Básico de Jogo - Pygame")


PRETO = (0,0,0)
nave = pygame.transform.scale((pygame.image.load('nave.png')),(50,50))
# Configurações do jogador
jogador_largura, jogador_altura = 50, 50
jogador_x, jogador_y = nave.get_size()
velocidade = 5

# Loop principal do jogo
clock = pygame.time.Clock()
rodando = True
tiro = pygame.transform.scale((pygame.image.load('bullet.png')),(220,220))
while rodando:
    # Controle de FPS
    clock.tick(60)
    if rodando:
        if jogador_y < 0:
            jogador_y = 0
        if jogador_y + jogador_altura > ALTURA:
            jogador_y = ALTURA - jogador_altura
        if jogador_x < 0:
            jogador_x = 0
        if jogador_x + jogador_largura> LARGURA:
            jogador_x = LARGURA - jogador_largura
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Controles do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        jogador_y -= velocidade
    if teclas[pygame.K_DOWN]:
        jogador_y += velocidade
    if teclas[pygame.K_LEFT]:
        jogador_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        jogador_x += velocidade
    

    # Lógica do jogo

    # Desenho na tela
    tela.fill(PRETO)  # Fundo preto
    tela.blit(nave,(jogador_x,jogador_y))  # Jogador
    pygame.display.flip()  # Atualiza a tela

# Encerra o jogo
pygame.quit()
sys.exit()
