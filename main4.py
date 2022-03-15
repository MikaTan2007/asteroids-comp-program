import pygame
import os
import time
import random

pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Space Shooter")

x = 50
y = 50
width = 40
height = 60
vel = 3
black = (0, 0, 0)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
"""pygame.mixer.music.load("explosion.mp3")
pygame.mixer.music.load("lazer1.wav")
pygame.mixer.music.load("lazer2.wav")
pygame.mixer.music.load("lazer3.wav")"""

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

#Explosion Frames
explosion1 = pygame.image.load('explosion1.png').convert()
explosion2 = pygame.image.load('explosion2.png').convert()
explosion3 = pygame.image.load('explosion3.png').convert()
explosion4 = pygame.image.load('explosion4.png').convert()

game_over = pygame.image.load('game_over3.png').convert()

sprite_list = [starship_base, starship_1, starship_2, starship_3, asteroid_1, asteroid_2, asteroid_3, explosion1, explosion2, explosion3, explosion4, game_over]
starship_list = [starship_base, starship_1, starship_2, starship_3]
explosion_list = [explosion1, explosion2, explosion3, explosion4]

for sprite in sprite_list:
    sprite.set_colorkey((0,0,0))

asteroid_1 = pygame.transform.scale(asteroid_1,(200,200))
asteroid_2 = pygame.transform.scale(asteroid_2,(200,200))
asteroid_3 = pygame.transform.scale(asteroid_3,(200,200))

starship_base = pygame.transform.scale(starship_base,(100,100))
starship_1 = pygame.transform.scale(starship_1,(100,100))
starship_2 = pygame.transform.scale(starship_2,(100,100))
starship_3 = pygame.transform.scale(starship_3,(100,100))
game_over = pygame.transform.scale(game_over,(800,800))

#Sprite Changing for StarShip
starship_sprites = [starship_1, starship_2, starship_3]
current_img_index = 0

explosion_index = 0

asteroid_id_num = 0

def spawn_asteroid():
    global asteroid_id_num
    asteroid_list = [asteroid_1, asteroid_2, asteroid_3]
    asteroid_num = random.randint(0,2)
    asteroid_sprite = asteroid_list[asteroid_num]

    #x = random.randint(0,800) - int(asteroid_sprite.get_width() / 2)
    #y = -60 - int(asteroid_sprite.get_width() / 2)

    asteroidXPos = random.randint(0,800)
    asteroidYPos = -10

    speed = (random.randint(-30,30)/100, random.randint(50,150)/100)

    size = random.randint(50,250)

    speed_of_rotation = random.randint(5,100)/100

    ###########
    #         #
    #         #
    #         #  
    ###########
    id_num = asteroid_id_num
    asteroid_id_num += 1
    #bottom_top_left = (asteroidYPos, asteroidYPos + size)
    #top_left_right = (asteroidXPos, asteroidXPos + size)

    health = size * 10

    asteroid_data.append([asteroid_sprite, asteroidXPos, asteroidYPos, speed, speed_of_rotation, 0, size, id_num, health])

def spawn_blaster(blaster_size, color):
    damage = blaster_size * 30
    blaster_data.append([x_pos + 50, y_pos, blaster_size, color, damage])

score = 0

blaster_data = [

]


    

    

clock = pygame.time.Clock()
time_counter = 0

start_time = time.time()

timer = 0
asteroid_timer = 0
explosion_timer = 0


vel = 5

x_pos = 400 - int(starship_base.get_width() / 2)
y_pos = 725 - int(starship_base.get_height() / 2)

angle = 5
angle2 = -5

run = True

#"name" : [sprite_type, x, y, (x,y)_speed, speed_of_rotation, current_rotation, size, (rectangle properties)]

asteroid_data = [
    
]

#Healthbar Related
starship_health = 1000000 #1,000,000
bar_length = 400
bar_red = 0
bar_green = 255

blaster_counter = 0
blaster_type_index = 0
blaster_types = ["normal", "medium", "high"]
blaster_type_index_counter = 0

blaster_type_dict = {
    "normal": [10, 5, (235, 247, 0)],
    "medium": [25, 10, (35, 207, 67)],
    "high": [50, 15, (42, 191, 189)]
}

while run:

    

    asteroid_rects = [

    ]

    time_counter = clock.tick(60)
    timer += time_counter
    asteroid_timer += time_counter
    explosion_timer += time_counter

    win.fill((0,255,0))

    win.blit(space_background,(400-int(space_background.get_width() / 2),400-int(space_background.get_height()/2)))

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #mx, my = pygame.mouse.get_pos()

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

    starship_rect.centerx = x_pos + int(starship_rect.width/2)
    starship_rect.centery = y_pos + int(starship_rect.width/2)

    starship_rect = pygame.Rect(starship_rect)

    win.blit(starship_sprites[current_img_index], (x_pos, y_pos))

    keys = pygame.key.get_pressed()

    blaster_type = blaster_type_dict[blaster_types[blaster_type_index]]

    blaster_type_timer = blaster_type[0]

    if keys[pygame.K_SPACE] == True:
        blaster_counter += 1 
        if blaster_counter > blaster_type_timer:
            spawn_blaster(blaster_type[1], blaster_type[2])
            if blaster_type[0] == 10:
                pygame.mixer.music.load("lazer1.wav")
                pygame.mixer.music.play(0)
            elif blaster_type[0] == 25:
                pygame.mixer.music.load("lazer2.wav")
                pygame.mixer.music.play(0)
            else:
                pygame.mixer.music.load("lazer3.wav")
                pygame.mixer.music.play(0)

            blaster_counter = 0

            
    else:
        blaster_counter += 1
    
    
    
    if keys[pygame.K_q] == True:
        blaster_type_index_counter += 1
        if blaster_type_index_counter > 10:
            blaster_type_index += 1
            if blaster_type_index > 2:
                blaster_type_index = 0
            blaster_type_index_counter = 0
    else:
        blaster_type_index_counter += 1
    

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
    
    #elif keys[pygame.K_SPACE] == True:
        #spawn_blaster()
    
    for blaster in blaster_data:
        blasterX = blaster[0]
        blasterY = blaster[1]
        blasterSize = blaster[2]
        blasterColor = blaster[3]
        pygame.draw.circle(win, blasterColor, (blasterX, blasterY), blasterSize)
        blaster[1] -= 10

    for asteroids in asteroid_data:

        asteroid_sprite = asteroids[0]
        asteroidXPos = asteroids[1]
        asteroidYPos = asteroids[2]
        x_speed = asteroids[3][0]
        y_speed = asteroids[3][1]
        

        size = asteroids[6]
        original_health = size * 10
        current_health = asteroids[8]

        id_num = asteroids[7]

        speed_of_angle = asteroids[4]

        current_rotation = asteroids[5]

        asteroid_sprite = pygame.transform.scale(asteroid_sprite,(size,size))
        asteroid_copy = pygame.transform.rotate(asteroid_sprite, current_rotation)
        asteroid_sprite_rect = asteroid_sprite.get_rect()
        
        asteroids[5] += speed_of_angle

        if asteroids[1] - 1/2*size  < -150 or asteroids[1] - 1/2*size > 800 or asteroids[2]- 1/2*size > 800:
            asteroid_data.remove(asteroids)

        

        asteroid_rects.append([(asteroidXPos, asteroidYPos), size, id_num])

        win.blit(asteroid_copy,(asteroidXPos - int(asteroid_copy.get_width()/2), asteroidYPos - int(asteroid_copy.get_width()/2)))

        asteroids[1] += x_speed
        asteroids[2] += y_speed

        bar_width = current_health/original_health
        bar_width = 50*bar_width

        pygame.draw.rect(win, (255,0,0), (asteroids[1] - 25, asteroids[2] - (size/2) + 25, bar_width, 10))

        #pygame.draw.rect(win, (bar_red,bar_green,0), (25, 25, 400, 50) , 1)
        

        

    for asteroid in asteroid_rects:
        
        asteroidXPos = asteroid[0][0]
        asteroidYPos = asteroid[0][1]
        asteroidSize = asteroid[1]

        asteroidXPos -= asteroidSize/4
        asteroidYPos -= asteroidSize/4
        asteroidSize = asteroidSize/2

        id_num = asteroid[2]

        #pygame.draw.rect(win, (0,0,255), (asteroidXPos, asteroidYPos, 10, 10) ,1)
        pygame.draw.rect(win, (0,0,255), (asteroidXPos, asteroidYPos, asteroidSize, asteroidSize) ,1)
        #pygame.draw.rect(win, (255,0,0), (asteroidXPos - asteroidSize/4, asteroidYPos - asteroidSize/4, asteroidSize/2, asteroidSize/2) ,1)

        if asteroidYPos + asteroidSize > y_pos and asteroidYPos + asteroidSize < y_pos + 180:
            asteroid_width = (asteroidXPos, asteroidXPos+asteroidSize)
            starship_width = (x_pos, x_pos + 100)
            count_up = x_pos
            while count_up < starship_width[1]:
                if count_up >= asteroid_width[0] and count_up <= asteroid_width[1]:
                    pygame.mixer.music.load("explosion.mp3")
                    pygame.mixer.music.play(0)
                    
                    if explosion_timer > 500:
                        
                        starship_health -= asteroidSize * 2

                        bar_red += 0.000255 * asteroidSize * 2
                        bar_green -= 0.000255 * asteroidSize * 2

                        if bar_red > 255 and bar_green < 0:
                            bar_red = 255
                            bar_green = 0


                        explosion_index = (explosion_index + 1) % 4

                        win.blit(explosion_list[explosion_index], (x_pos,y_pos))
                        
                        timer = 0
                    
                count_up += 1

        for blaster in blaster_data:
            #asteroidYPos + asteroidSize > blaster[0] and asteroidYPos + asteroidSize < blaster[1]
            blasterX = blaster[0]
            blasterY = blaster[1]
            if blasterX + 10 > asteroidXPos and blasterX -  10 < asteroidXPos + asteroidSize and blasterY > asteroidYPos and blasterY < asteroidYPos + asteroidSize:
                blaster_data.remove(blaster)
                for asteroids in asteroid_data:
                    if id_num == asteroids[7]:
                        asteroids[8] -= blaster[4]
                        
                        if asteroids[8] <= 0:
                            asteroid_data.remove(asteroids)
                            score += size * 3
                            print(score)
            elif blasterY < 0:
                blaster_data.remove(blaster)
             
        
                
        

    pygame.draw.rect(win, (255,0,0), (x_pos, y_pos, 100, 100) ,1)

    bar_width = starship_health/1000000
    bar_width = 400*bar_width

    pygame.draw.rect(win, (bar_red,bar_green,0), (25, 25, bar_width, 50))

    pygame.draw.rect(win, (bar_red,bar_green,0), (25, 25, 400, 50) , 1)
    
    
    if bar_width < 0:
        bar_width = 0
        win.blit(game_over,(400-int(game_over.get_width() / 2),400-int(game_over.get_height()/2)))
    
    

    
    
    pygame.display.update() 
    
pygame.quit()