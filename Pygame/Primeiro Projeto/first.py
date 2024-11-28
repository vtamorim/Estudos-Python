import pygame
from sys import exit
from random import randint

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('ue.png').convert_alpha()
		player_walk_2 = pygame.image.load('ue2.png').convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2]
		self.player_index = 0
		self.player_jump = pygame.image.load('ue3.png').convert_alpha()

		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,100))
		self.gravity = 0

		self.jump_sound = pygame.mixer.Sound('jump.mp3')
		self.jump_sound.set_volume(0.5)

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 350:
			self.gravity = -20
			self.jump_sound.play()

	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 350:
			self.rect.bottom = 350

	def animation_state(self):
		if self.rect.bottom < 350: 
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk):self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]

	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		
		if type == 'fly':
			fly_1 = pygame.image.load('uemano.png').convert_alpha()
			fly_2 = pygame.image.load('uemano2.png').convert_alpha()
               
			self.frames = [fly_1,fly_2]
			y_pos = 210
		else:
			snail_1 = pygame.image.load('caracol.png').convert_alpha()
			snail_2 = pygame.image.load('caracol2.png').convert_alpha()
			self.frames = [snail_1,snail_2]
			y_pos  = 300

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

	def animation_state(self):
		self.animation_index += 0.1 
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.animation_state()
		self.rect.x -= 6
		self.destroy()

	def destroy(self):
		if self.rect.x <= -100: 
			self.kill()
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return current_time


def movement_obs(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 350:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    return []


def check_collisions(player_rect, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player_rect.colliderect(obstacle_rect):
                return False
    return True


def update_player_animation():
    global player_surf, player_index
    if player_rect.bottom < 350:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


# Inicialização
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pixel Runner")
clock = pygame.time.Clock()
font = pygame.font.Font('fontezinhaui.ttf', 50)

# Estados do jogo
game_active = False
start_time = 0
score = 0

# Fundo e chão
background = pygame.transform.scale(pygame.image.load('OIP.jfif'), (800, 360)).convert_alpha()
ground = pygame.transform.scale(pygame.image.load('R.png'), (800,90)).convert_alpha()

# Obstáculos
snail1 = pygame.image.load('caracol.png').convert_alpha()
snail2 = pygame.image.load('caracol2.png').convert_alpha()
snail_frames = [snail1, snail2]
snail_index = 0
snail_surf = snail_frames[snail_index]

fly1 = pygame.image.load('uemano.png').convert_alpha()
fly2 = pygame.image.load('uemano2.png').convert_alpha()
fly3 = pygame.image.load('uemano3.png').convert_alpha()
fly_frames = [fly1, fly2, fly3]
fly_index = 0
fly_surf = fly_frames[fly_index]

# Jogador
player1 = pygame.image.load('ue.png').convert_alpha()
player2 = pygame.image.load('ue2.png').convert_alpha()
player_walk = [player1, player2]
player_index = 0
player_surf = player_walk[player_index]
player_jump = pygame.image.load('ue3.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 350))

# Tela inicial
player_stand = pygame.image.load('ue.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand, (140, 280))
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 50))

game_message = font.render('Press SPACE to start', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 350))

# Gravidade e obstáculos
player_gravity = 0
obstacle_list = []

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

# Loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 350:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 350:
                    player_gravity = -20
            if event.type == obstacle_timer:
                if randint(0, 1):
                    obstacle_list.append(snail_surf.get_rect(bottomright=(randint(900, 1100), 350)))
                else:
                    obstacle_list.append(fly_surf.get_rect(bottomright=(randint(900, 1100), 280)))
            if event.type == snail_animation_timer:
                snail_index = (snail_index + 1) % len(snail_frames)
                snail_surf = snail_frames[snail_index]
            if event.type == fly_animation_timer:
                fly_index = (fly_index + 1) % len(fly_frames)
                fly_surf = fly_frames[fly_index]
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(background, (0, 0))
        screen.blit(ground, (0,350))
        score = display_score()

        # Jogador
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 350:
            player_rect.bottom = 350
        update_player_animation()
        screen.blit(player_surf, player_rect)

        # Obstáculos
        obstacle_list = movement_obs(obstacle_list)

        # Colisões
        game_active = check_collisions(player_rect, obstacle_list)
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_list.clear()
        player_rect.midbottom = (80, 350)
        player_gravity = 0

        screen.blit(game_name, game_name_rect)
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            score_message = font.render(f'Your Score: {score}', False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center=(400, 330))
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
