import pygame
import random

 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,0,0)
BLUE = (0,0,255)

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

player_x = 0
player_y = 0
player_w = 50
player_h = 50

block_x = []
block_y = []
#boss_x = [] 
#boss_y = []
#boss  =  []
collisions = []
for i in range(10):
    block_x.append(random.randrange(screen_width))
    block_y.append(random.randrange(screen_height))
    collisions.append(False)
'''    
for i in range(10):
    boss_x.append(random.randrange(screen_width))
    boss_y.append(random.randrange(screen_height))
    boss.append(False)
'''  
block_w = 50
block_h = 50
score = 0
font = pygame.font.Font(None, 50)

done = False

clock = pygame.time.Clock()
start_ticks=pygame.time.get_ticks() 

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 

    screen.fill(WHITE)
    
    seconds=int((pygame.time.get_ticks()-start_ticks)/1000)
   
    pos = pygame.mouse.get_pos()

    for i in range(10):
        xin = block_x[i]<=player_x<=block_x[i]+block_w or block_x[i]<=player_x+player_w<=block_x[i]+block_w
        yin = block_y[i]<=player_y<=block_y[i]+block_h or block_y[i]<=player_y+player_h<=block_y[i]+block_h
        if  xin and yin and not collisions[i]:
            collisions[i] = True
            score += 1       
    '''    
    for i in range(10):
        boss_x = boss_x[i]<=player_x<=boss_x[i]+block_w or boss_x[i]<=player_x+player_w<=boss_x[i]+block_w
        boss_y =  boss_y[i]<=player_y<=boss_y[i]+block_h or boss_y[i]<=player_y+player_h<=boss_y[i]+block_h
        if  boss_x  and  boss_y and not boss[i]:
            boss[i] = True
    '''         
    player_x = pos[0]
    player_y = pos[1]
    pygame.draw.rect(screen, RED, [player_x, player_y, player_w, player_h])
    for i in range(10):
        if not collisions[i]:
            pygame.draw.rect(screen, BLACK, [block_x[i], block_y[i], block_w, block_h])

            
            if block_y[i] == block_y[i]:   
                   block_y[i]+=5 
                   
            if block_y[i]>700:
                block_y[i]=2
    '''         
    for i in range(10):
        if not boss[i]:
            pygame.draw.rect(screen, BLUE, [block_x[i], block_y[i], block_w, block_h])
            text = font.render("GAME OVER", 50, BLACK)
            screen.blit(text, (100,100))   
     '''       
    message = str(score)+' point'
    text = font.render(message, 10, BLACK)
    screen.blit(text, (10,10))
    
    t = font.render(str(seconds), 10, RED)
    screen.blit(t, (40,40))
    
    if seconds>10:
        text = font.render("GAME OVER", 50, BLACK)
        screen.blit(text, (100,100))
        done=True
    if score==10:
        text = font.render("YOU WIN!!!", 50, BLACK)
        screen.blit(text, (100,100))
        done=True

    pygame.display.flip()

    clock.tick(60)

pygame.quit()