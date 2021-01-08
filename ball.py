import pygame
import math
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, speed, srx, sry, r, color,edge=10):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([r*2, r*2])
        self.image.fill(BLACK)
        pygame.draw.circle(self.image, color, (r,r), r, edge)
        self.rect = self.image.get_rect()
        self.rect.center = (srx,sry)
        direction = random.randint(20,70)  
        radian = math.radians(direction)  
        self.dx = speed * math.cos(radian)  
        self.dy = -speed * math.sin(radian)
     
    def collideB(self):
        self.dx *= -1
    def Bup(self): 
        self.dy *= -1  
    def BLR(self):
        self.dx *= -1    
        
    def up(self):
        self.x += self.dx  
        self.y += self.dy
        self.rect.x = self.x  
        self.rect.y = self.y
        
        if self.rect.top <= 5:  
                self.Bup()
        if self.rect.bottom >= screen.get_height()-5:
            return True
        else:
            return False
    

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

clock = pygame.time.Clock()
play = True

while play:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            play = False 

    screen.fill(WHITE)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()




