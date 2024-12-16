import pygame
import sys
import random

pygame.init()


width, height = 1200, 600
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Shooter - Basic")


PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)


nave = pygame.transform.scale(pygame.image.load('nave.png'), (50, 50))
inimigo = pygame.transform.scale(pygame.image.load('qfoi.png'), (50, 50))
tiro = pygame.transform.scale(pygame.image.load('bullet.png'), (5, 5))
fundo = pygame.transform.scale(pygame.image.load('eae.jpg'), (width, height)).convert_alpha()


jogador_width, jogador_height = 50, 50
jogador_x, jogador_y = width // 2, height - jogador_height - 10
jogador_vel_x, jogador_vel_y = 0, 0
velocidade = 0.5


inimigo_x, inimigo_y = random.randint(0, width - 50), 100
inimigo_vel_x, inimigo_vel_y = 2, 2


tiros_principal = []
tiros_inimigo = []


ganhou = None
perdeu = None


ultimo_tiro_principal = 0
ultimo_tiro_inimigo = 0
intervalo_tiros_principal = 200  
intervalo_tiros_inimigo = 1000  


clock = pygame.time.Clock()


def atirar_principal():
    novo_tiro = tiro.get_rect(center=(jogador_x + jogador_width // 2, jogador_y))
    tiros_principal.append(novo_tiro)

def atirar_inimigo():
    inim_tiro = tiro.get_rect(center=(inimigo_x + 25, inimigo_y + 50))
    tiros_inimigo.append(inim_tiro)

def comecar_jogo():
    global jogador_x, jogador_y, inimigo_x, inimigo_y, tiros_principal, tiros_inimigo, ganhou, perdeu
    jogador_x, jogador_y = width // 2, height - jogador_height - 10
    inimigo_x, inimigo_y = random.randint(0,10),0
    tiros_principal.clear()
    tiros_inimigo.clear()
    ganhou = None
    perdeu = None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        jogador_y -= velocidade
    if teclas[pygame.K_DOWN]:
        jogador_y += velocidade
    if teclas[pygame.K_LEFT]:
        jogador_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        jogador_x += velocidade

    if teclas[pygame.K_w]:
        jogador_vel_y -= velocidade
    if teclas[pygame.K_s]:
        jogador_vel_y += velocidade
    if teclas[pygame.K_a]:
        jogador_vel_x -= velocidade
    if teclas[pygame.K_d]:
        jogador_vel_x += velocidade
    if teclas[pygame.K_SPACE] and pygame.time.get_ticks() - ultimo_tiro_principal > intervalo_tiros_principal:
        atirar_principal()
        ultimo_tiro_principal = pygame.time.get_ticks()



    jogador_x += jogador_vel_x
    jogador_y += jogador_vel_y
    jogador_vel_x *= 0.9
    jogador_vel_y *= 0.9


    jogador_x = max(0, min(jogador_x, width - jogador_width))
    jogador_y = max(0, min(jogador_y, height - jogador_height))


    inimigo_x += inimigo_vel_x
    inimigo_y += inimigo_vel_y
    if inimigo_x <= 0 or inimigo_x + 50 >= width:
        inimigo_vel_x *= -1
    if inimigo_y <= 0 or inimigo_y + 50 >= height:
        inimigo_vel_y *= -1


    if pygame.time.get_ticks() - ultimo_tiro_inimigo > intervalo_tiros_inimigo:
        atirar_inimigo()
        ultimo_tiro_inimigo = pygame.time.get_ticks() - 600


    for tiro_rect in tiros_principal[:]:
        tiro_rect.y -= 10
        if tiro_rect.y < 0:
            tiros_principal.remove(tiro_rect)
        elif tiro_rect.colliderect(pygame.Rect(inimigo_x, inimigo_y, 50, 50)):
            ganhou = True
            tiros_principal.remove(tiro_rect)

    for inim_tiro in tiros_inimigo[:]:
        inim_tiro.y += 10
        if inim_tiro.y > height:
            tiros_inimigo.remove(inim_tiro)
        elif inim_tiro.colliderect(pygame.Rect(jogador_x, jogador_y, jogador_width, jogador_height)):
            perdeu = True
            tiros_inimigo.remove(inim_tiro)

    if ganhou or perdeu:
        tela.fill(PRETO)
        font = pygame.font.Font('mudaissopfv.ttf',60)
        text = font.render('ean', True, (255,255,255), (255,255,255))
        textRect = text.get_rect()
        textRect.center = (width // 2 - 30, height //2 - 30)
        if perdeu:
            text = font.render('Bixo burro', True, (255,0,0),False)
        elif ganhou:
            text = font.render('Ganhou', True, (0,255,0),False)
        tela.blit(text,textRect)
        if teclas[pygame.K_r]:
            comecar_jogo()
        pygame.display.update()
        continue
    else:
        tela.blit(fundo, (0, 0))
        tela.blit(nave, (jogador_x, jogador_y))
        tela.blit(inimigo, (inimigo_x, inimigo_y))
    for tiro_rect in tiros_principal:
        tela.blit(tiro, tiro_rect)
    for inim_tiro in tiros_inimigo:
        tela.blit(tiro, inim_tiro)

    pygame.display.update()
    clock.tick(60)
