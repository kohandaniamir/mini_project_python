import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800 , 600
BALL_SPEED = 7
PADDLE_SPEED = 7
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
score1 = 0
score2 = 0
player1_name = "A"
player2_name = "B"
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
paddle1 = pygame.Rect(50, HEIGHT // 2 - 60, 10, 120)
paddle2 = pygame.Rect(WIDTH - 60, HEIGHT // 2 -60, 10, 120)
ball_dx = BALL_SPEED * random.choice((1, -1))
ball_dy = BALL_SPEED * random.choice((1, -1))
paddle1_dy = 0
paddle2_dy = 0
ball_in_motion = True
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ping Pong")

def drow_scores():
    font = pygame.font.Font(None,36)
    score1_text =font.render(f"{player1_name}:{score1}",True,GREEN)
    score2_text = font.render(f"{player2_name}:{score2}", True, GREEN)
    screen.blit(score1_text,(10,10))
    screen.blit(score1_text, (WIDTH-score2_text.get_width() -10 ,10))

def check_collision(ball,paddle):
    if ball.colliderect(paddle):
        return True
    return False

def reset_ball_position():
    side = random.choice(("left,right"))
    if side == "left":
        ball.x = 10 + 50 + 10
        ball_dx = BALL_SPEED
    else:
        ball.x = WHITE -50 -10 -30 -10
        ball_dx = -BALL_SPEED
    ball_dy = HEIGHT // 2 - 15
    return ball_dx

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle2_dy = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                paddle2_dy = PADDLE_SPEED
            elif event.key == pygame.K_SPACE:
                ball_in_motion = True