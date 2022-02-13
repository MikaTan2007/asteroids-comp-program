from turtle import speed
import pygame
import os
import time
import random

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

#Background
space_background = pygame.image.load('background.png').convert() 

#Base Starship + Sprite Animations of it
starship_base = pygame.image.load('starship1.png').convert()
starship_1 = pygame.image.load('starship2.png').convert()
starship_2 = pygame.image.load('starship3.png').convert()
starship_3 = pygame.image.load('starship4.png').convert()

#Asteroids
asteroid_1 = pygame.image.load('asteroid1.png').convert()
asteroid_2 = pygame.image.load('asteroid2.png').convert()
asteroid_3 = pygame.image.load('asteroid3.png').convert()

sprite_list = [starship_base, starship_1, starship_2, starship_3, asteroid_1, asteroid_2, asteroid_3]
starship_list = [starship_base, starship_1, starship_2, starship_3]

for sprite in sprite_list:
    sprite.set_colorkey((0,0,0))

asteroid_1 = pygame.transform.scale(asteroid_1,(200,200))
asteroid_2 = pygame.transform.scale(asteroid_2,(200,200))
asteroid_3 = pygame.transform.scale(asteroid_3,(200,200))

starship_base = pygame.transform.scale(starship_base,(100,100))
starship_1 = pygame.transform.scale(starship_1,(100,100))
starship_2 = pygame.transform.scale(starship_2,(100,100))
starship_3 = pygame.transform.scale(starship_3,(100,100))

#Sprite Changing for StarShip
starship_sprites = [starship_1, starship_2, starship_3]
current_img_index = 0

def spawn_asteroid():
    asteroid_list = [asteroid_1, asteroid_2, asteroid_3]
    asteroid_num = random.randint(0,2)
    asteroid_sprite = asteroid_list[asteroid_num]

    #x = random.randint(0,800) - int(asteroid_sprite.get_width() / 2)
    #y = -60 - int(asteroid_sprite.get_width() / 2)

    asteroidXPos = random.randint(0,800)
    asteroidYPos = 50

    speed = (random.randint(-30,30)/100, random.randint(30,80)/100)

    size = random.randint(50,250)

    speed_of_rotation = random.randint(5,100)/100

    asteroid_data.append([asteroid_sprite, asteroidXPos, asteroidYPos, speed, speed_of_rotation, 0, size])
    

clock = pygame.time.Clock()
time_counter = 0

start_time = time.time()

timer = 0
asteroid_timer = 0

vel = 5

x_pos = 400 - int(starship_base.get_width() / 2)
y_pos = 725 - int(starship_base.get_height() / 2)

angle = 5
angle2 = -5

run = True

#"name" : [sprite_type, x, y, (x,y)_speed, speed_of_rotation, current_rotation, size, (rectangle properties)]

asteroid_data = [
    
]

asteroid_rects = [ 

]

while run:

    asteroid_rects = [

    ]

    time_counter = clock.tick(60)
    timer += time_counter
    asteroid_timer += time_counter

    win.fill((0,255,0))

    win.blit(space_background,(400-int(space_background.get_width() / 2),400-int(space_background.get_height()/2)))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    mx, my = pygame.mouse.get_pos()

    #Sprite Changing
    if timer > 200:
        
        
        current_img_index = (current_img_index + 1) % 3 

        #mx, my = pygame.mouse.get_pos()
        #win.blit(starship_sprites[current_img_index], (mx - int(starship_base.get_width() / 2), my - int(starship_base.get_height() / 2)))
        
        # Reset the timer
        timer = 0
    
    #Asteroid Spawning
    if asteroid_timer > 1000:

        spawn_asteroid()
        asteroid_timer = 0

    


    starship_rect = starship_base.get_rect()

    win.blit(starship_sprites[current_img_index], (x_pos, y_pos))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] == True and x_pos > 0:
        win.blit(space_background,(400-int(space_background.get_width() / 2),400-int(space_background.get_height()/2)))

        img_copy = pygame.transform.rotate(starship_sprites[current_img_index], angle)

        x_pos -= vel

        
        win.blit(img_copy, (x_pos, y_pos))

    elif keys[pygame.K_RIGHT] == True and x_pos < 700:
        win.blit(space_background,(400-int(space_background.get_width() / 2),400-int(space_background.get_height()/2)))

        img_copy = pygame.transform.rotate(starship_sprites[current_img_index], angle2)

        x_pos += vel

        
        win.blit(img_copy, (x_pos, y_pos))

    for asteroids in asteroid_data:

        asteroid_sprite = asteroids[0]
        asteroidXPos = asteroids[1]
        asteroidYPos = asteroids[2]
        x_speed = asteroids[3][0]
        y_speed = asteroids[3][1]

        size = asteroids[6]

        speed_of_angle = asteroids[4]

        current_rotation = asteroids[5]

        asteroid_sprite = pygame.transform.scale(asteroid_sprite,(size,size))
        asteroid_copy = pygame.transform.rotate(asteroid_sprite, current_rotation)
        asteroid_sprite_rect = asteroid_sprite.get_rect()
        
        asteroids[5] += speed_of_angle

        win.blit(asteroid_copy,(asteroidXPos - int(asteroid_copy.get_width()/2), asteroidYPos - int(asteroid_copy.get_width()/2)))

        asteroids[1] += x_speed
        asteroids[2] += y_speed
        
        rectangle = (asteroidXPos - int(asteroid_sprite_rect.width/4), asteroidYPos - int(asteroid_sprite_rect.height/4), asteroid_sprite_rect.width/2, asteroid_sprite_rect.height/2)
        #pygame.draw.rect(win, (255,0,0), (asteroidXPos - int(asteroid_sprite_rect.width/4), asteroidYPos - int(asteroid_sprite_rect.height/4), asteroid_sprite_rect.width/2, asteroid_sprite_rect.height/2) ,1)
        
        
        if len(asteroids) != 8:
            asteroids.append(pygame.Rect(rectangle))
        
        pygame.draw.rect(win, (255,0,0), rectangle ,1)
    
    asteroid_rect_list = [

    ]

    for asteroid in asteroid_data:
        asteroid_rect_list.append(asteroid[7])

    asteroid_rect_index = 0
    for asteroids in asteroid_rect_list:
        asteroid_rect_list.remove(asteroids)
        for asteroid2 in asteroid_rect_list:
           if pygame.Rect.colliderect(asteroids, asteroid2):
               


        else:
            asteroid_rect_list.insert(asteroid_rect_index, asteroids)
        
        asteroid_rect_index += 1



    """for rect in asteroid_rects:
        asteroid_rects.remove(rect)
        if (pygame.Rect.collidelist(rect, asteroid_rects) != -1):
            asteroid_data.remove(asteroid_data[rect_index])
            #print(asteroid_rects[pygame.Rect.collidelist(rect, asteroid_rects)])
            #print(asteroid_data[rect_index])
        #print(rect, "----", asteroid_data[rect_index])
        rect_index += 1"""
    
    """for rect in asteroid_rects:
        asteroid_rects.remove(rect)
        for rect2 in asteroid_rects:
            if pygame.Rect.colliderect(rect, rect2) == True:
                asteroid_data.remove(asteroid_data[rect_index])
                for other_rect in asteroid_rects:
                    if other_rect == rect2:
                        asteroid_data.remove(asteroid_data[rect_index])
                        asteroid_data.remove(asteroid_data[num])
                        asteroid_rects.remove(rect2)
                    num += 1
        rect_index += 1"""
        

    pygame.draw.rect(win, (255,0,0), (x_pos,y_pos, 100, 100), 1)
    
    pygame.display.update() 
    
pygame.quit()