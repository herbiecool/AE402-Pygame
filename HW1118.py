import pygame
import random
pygame.init()

windowSize = [700, 500]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()
white=(255,255,255)
black = (0,0,0)
'''
def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)
'''

def random_color():
    a=random.randint(0,255)
    b=random.randint(0,255)
    c=random.randint(0,255)
    d=a
    return d

count = 0
click = False 
limit = 30 
pos = (0, 0)
count = 0
click = False 
limit = 30 

pos = (0, 0)

done = False
while not done:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click = True
            count = 0            
     
        if event.type == pygame.QUIT:
            done = True
    if click:
        pygame.draw.circle(screen, random_color(), pos, count)
        count += 1

    pygame.display.flip()
    clock.tick(60)
pygame.quit()