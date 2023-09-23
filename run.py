import pygame
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
SPEED = 10

class Bird(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.images = [pygame.image.load('bluebird-upflap.png').convert_alpha(),
                       pygame.image.load('bluebird-midflap.png').convert_alpha(),
                       pygame.image.load('bluebird-downflap.png').convert_alpha()]
        
        self.current_image = 0 
        
        self.image = pygame.image.load('bluebird-midflap.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGHT / 2
    
    def update(self):
        self.current_image = (self.current_image + 1) % 3 
        self.image = self.images[ self.current_image]
        pass
    
    # Update height
        self.rect[1] += SPEED
    





pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')


bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    screen.blit(BACKGROUND, (0, 0))
    
    bird_group.update()
    bird_group.draw(screen)
    
    
    pygame.display.update()
    