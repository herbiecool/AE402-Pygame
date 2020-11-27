import pygame
white = (255,255,255)
black = (0,0,0)

pygame.init()
window_size = (800,600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Herbie_image')

done = False

clock = pygame.time.Clock()
player_image = pygame.image.load("C:\\Users\\redno\\Desktop\\image\\player.png")
background_image = pygame.image.load("C:\\Users\\redno\\Desktop\\image\\space.jpg")
player_image.convert( )
fire = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire = True
                x,y = pygame.mouse.get_pos()
    a,b = pygame.mouse.get_pos()
    screen.fill(white)
    screen.blit(background_image,(0,0))
    if fire:
        y-=5
        pygame.draw.circle(screen,white,(x+50,y-20),10)
        
    screen.blit(player_image,(a,b))
    pygame.display.flip()
    clock.tick(40)

pygame.quit()