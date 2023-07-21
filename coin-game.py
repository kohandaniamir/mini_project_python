import pygame
import random

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("بازی سکه و مانع")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow =(255,255,0)
dark_gray =(40,40,40)
light_gray =(120,120,120)


player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 10


obstacle_width = 100
obstacle_height = 20
obstacle_x = random.randint(0,screen_width-obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 3
obstacle_speed_increase = 0.2

coin_radius = 15
coin_x = random.randint(coin_radius,screen_width-coin_radius)
coin_y = -coin_radius
coin_speed = 4
coin_speed_increase = 0.2

clock = pygame.time.Clock()

score =0

normal_font = pygame.font.Font(None,40)
game_over_font =pygame.font.Font(None,80)

dark_mode = True

running = True
game_over =False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                player_x = screen_width // 2 - player_width // 2
                player_y = screen_height - player_height - 10
                coin_x = random.randint(coin_radius, screen_width - coin_radius)
                coin_y = -coin_radius
                obstacle_speed = 3
                coin_x = random.randint(coin_radius, screen_width - coin_radius)
                coin_y = -coin_radius
                coin_speed = 4
                score = 0
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0 :
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x > screen_width:
            player_x += player_speed


    pygame.display.update()
    clock.tick(60)


pygame.quit()