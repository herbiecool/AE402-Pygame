import pygame
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
RED=(255,0,0)
pygame.init()
screen_width = 700
screen_height = 400
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My game")

player_w = 50
player_h = 50
player_x = 
player_y = 

block_w = 50
block_h = 50
block_x = random.randrange(screen_width-block_w)
block_y = random.randrange(screen_height-block_h)
block_x = []
block_y = []
collision = []

for i in range(10):
    block_x.append(random.randrange(screen_width-block_w))
    block_y.append(random.randrange(screen_height-block_h))
    collision.append(False)



done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    xin = block_x<=player_x<=block_x+block_w or block_x<=player_x+player_w<=block_x+block_w
    yin = block_y<=player_y<=block_y+block_h or block_y<=player_y+player_h<=block_y+block_h
    
    collision = False
    
    score = 0
    
    if  xin and yin and not collision:
        collision = True
        score += 1
    for i in range(10):
        xin = block_x[i]<=player_x<=block_x[i]+block_w or block_x[i]<=player_x+player_w<=block_x[i]+block_w
        yin = block_y[i]<=player_y<=block_y[i]+block_h or block_y[i]<=player_y+player_h<=block_y[i]+block_h
        if  xin and yin and not collision[i]:
            collision[i] = True
            score += 1

    screen.fill(WHITE)

    player_x = [0]
    player_y = [1]
    pygame.draw.rect(screen, RED, [player_x, player_y, player_w, player_h])
    if not collision:
        pygame.draw.rect(screen, BLACK, [block_x, block_y, block_w, block_h])
    for i in range(10):
        if not collision[i]:
            pygame.draw.rect(screen, BLACK, [block_x[i], block_y[i], block_w, block_h])

    message = str(score)+' point'
