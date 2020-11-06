import pygame

Black = (0,0,0)
White = (255,255,255)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("my game")
done = False
clock = pygame.time.Clock()

x_pos = 100
y_pos = 100

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(White)
    pygame.draw.circle(screen,Black,(x_pos,y_pos),50,5)
    y_pos+=5
    x_pos+=5
    if y_pos and x_pos==550:
        y_pos=-50
        x_pos=-50
        
    pygame.display.flip()
    clock.tick(100)
    
pygame.quit()