import pygame
import os
import time
pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 3
black = (0, 0, 0)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
space_background = pygame.image.load('background.png').convert()
starship_base = pygame.image.load('starship1.png').convert()

starship_1 = pygame.image.load('starship2.png').convert()
starship_2 = pygame.image.load('starship3.png').convert()
starship_3 = pygame.image.load('starship4.png').convert()

asteroid1 = pygame.image.load('asteroid1.png').convert()
asteroid2 = pygame.image.load('asteroid2.png').convert()
asteroid3 = pygame.image.load('asteroid3.png').convert()



class background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(space_background, (800,800))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)

class starship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(starship_base, (150,150))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 700)
       

all_sprites = pygame.sprite.Group()
BackGround = background()
StarShip = starship()
all_sprites.add(BackGround)
all_sprites.add(StarShip)

def changeStarShip(StarShipSprite):
    StarShip.image = pygame.transform.scale(StarShipSprite, (150,150))
    StarShip.image.set_colorkey(black)
    

run = True

clock = pygame.time.Clock()
time_counter = 0

starship_sprites = [starship_2, starship_3, starship_1]

current_img_index = 0

start_time = time.time()

timer = 0

start = False

angle = 0 

while run:
    #angle += 1

    time_counter = clock.tick(60)
    timer += time_counter
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    """mx,my = pygame.mouse.get_pos()

    StarShip.rect.x = mx
    StarShip.rect.y = my"""

    
    if keys[pygame.K_SPACE]:
        start = True
    
    if keys[pygame.K_LEFT] and StarShip.rect.x > 0 and start == True:  
        #win.blit(starship_base,(100,100))
        #img_copy = pygame.transform.rotate(StarShip.image, angle)
        #StarShip.image = pygame.transform.rotate(StarShip.image, angle)
        StarShip.rect.x -= vel


    if keys[pygame.K_RIGHT] and StarShip.rect.x < 650 and start == True:  
        StarShip.rect.x += vel

    if keys[pygame.K_UP] and StarShip.rect.y > 15 and start == True: 
        StarShip.rect.y -= vel

    if keys[pygame.K_DOWN] and StarShip.rect.y < 650 and start == True:
        StarShip.rect.y += vel
    

    if timer > 500 and start == True:
        
        current_img_index = (current_img_index + 1) % 3 
        changeStarShip(starship_sprites[current_img_index])

        # Reset the timer
        timer = 0

    
    
    win.fill((0,0,0))
    all_sprites.update()
    all_sprites.draw(win)
    pygame.display.update() 
    
pygame.quit()