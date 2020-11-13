import pygame
import random
snowList = []

Black = (0,0,0)
White = (255,255,255)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("My game")
    
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  
          
    screen.fill(Black)

    for i in range(50):
        x = random.randrange(0,700)
        y = random.randrange(0,500)
        snowList.append([x,y])

    for i in range(50):
        pygame.draw.circle(screen,White,snowList[i],2)
        snowList[i][1]+=1
     if snowList[i][1]>500:
         snowList[i][1]=-2
    pygame.display.flip()
    clock.tick(100)
        
pygame.quit()