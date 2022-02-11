import pygame
import random
import sys
import os

from pygame.constants import K_LEFT, K_RIGHT

width = 800
length = 800

fps = 60

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, length))
pygame.display.set_caption("Pygame Python Test")
clock = pygame.time.Clock()

#sprite assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
starship_1 = pygame.image.load(os.path.join(img_folder, 'starship2.png')).convert()
background_sprite = pygame.image.load(os.path.join(img_folder, 'background.png')).convert()

#Class
class background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(background_sprite, (800,800))
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, length/2)

class starship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(starship_1, (300,300))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, length/2)
    

#Sprites
all_sprites = pygame.sprite.Group()
StarShip = starship()
BackGround = background()
#all_sprites.add(BackGround)
all_sprites.add(StarShip)

vel = 20

while True:
    # keep loop running at the right speed
    clock.tick(fps)
    # Process input (events)
    for event in pygame.event.get():
    
        # check for closing window
        if event.type == pygame.QUIT:
            sys.exit()
        
        keys = pygame.key.get_pressed()

    
        if keys[pygame.K_LEFT]:
            StarShip.rect.x -= vel

        if keys[pygame.K_RIGHT]:
            StarShip.rect.x += vel

        if keys[pygame.K_UP]:
            StarShip.rect.y -= vel

        if keys[pygame.K_DOWN]:
            StarShip.rect.y += vel



    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(white)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.update()

