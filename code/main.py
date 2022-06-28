import pygame
import random
import math
from pygame  import mixer
from player import Player
from bullet import Bullet
from enemy import Enemy

pygame.init() # Start pygame

screen = pygame.display.set_mode((682,512)) # Creates Screen

# mixer.music.load("../media/Doom.wav")
# mixer.music.play(-1)

# Title and Icon.
pygame.display.set_caption("Doom")
icon = pygame.image.load("../media/001-pentagram.png")
pygame.display.set_icon(icon)
background = pygame.image.load("../media/hell.jpg")

# FPS
clock = pygame.time.Clock()

# Start game.
running = True

# Character
player_walk_count = 0

# Faces
faces = ["../media/player/faces/doom-face1.png", "../media/player/faces/doom-face2.png", "../media/player/faces/doom-face1.png", "../media/player/faces/doom-face3.png", "../media/player/faces/doom-face1.png", "../media/player/faces/doom-face2.png", "../media/player/faces/doom-face1.png", "../media/player/faces/doom-face3.png", "../media/player/faces/doom-face1.png"]

# Setting up character
character = Player()

character.set_x(600)
character.set_y(300)
character.set_velocity(5)
character.set_height(64)
character.set_width(64)
character.set_last_direction("left")

# Setting up bullet
bullet = Bullet()

bullet.set_state("ready")
bullet.set_velocity(15)

# Character moving

x = character.get_x()
y = character.get_y()

frame = 0

def shoot(x, y):
    bullet.set_state("fire")
    screen.blit(pygame.image.load(bullet.get_image()), (x, y))
    
def redraw_screen():
    
    # background.
    screen.blit(background, (0,0))
    
    global player_walk_count
    global frame
    
    if player_walk_count + 1 >= 27:
        player_walk_count = 0

    if character.get_left():
        walk_left_animation = character.get_walkLeft_animation()
        screen.blit(pygame.image.load(walk_left_animation[player_walk_count//3]), (x, y))
        player_walk_count += 1
        
        screen.blit(pygame.image.load(faces[3]), (20, 20))
        
    elif character.get_right():
        
        walk_right_animation = character.get_walkRight_animation()
        screen.blit(pygame.image.load(walk_right_animation[player_walk_count//3]), (x,y))
        player_walk_count +=1
        
        screen.blit(pygame.image.load(faces[1]), (20, 20))
        
    else:
        if character.get_last_direction() == "left":
            doom_guy_img = character.get_image_l()
        elif  character.get_last_direction() == "right":
            doom_guy_img = character.get_image_r()
            
        screen.blit(pygame.image.load(doom_guy_img), (x,y))
        
        screen.blit(pygame.image.load(faces[0]), (20, 20))        
    
    if bullet.get_x() <= 0 or bullet.get_x() >= 682:
        bullet.set_x(character.get_x())
        bullet.set_state("ready")
    
    if bullet.get_state() == "fire":
        shoot(bullet.get_x(), bullet.get_y())
        
        if direction == "left":
            bullet_x = bullet.get_x() - bullet.get_velocity()
        else:
            bullet_x = bullet.get_x() + bullet.get_velocity()
        bullet.set_x(bullet_x)
    
    pygame.display.update()

while running:
    clock.tick(27)
    frame += 1
    
    # Anything persistant goes inside this loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
                
        x = character.get_x()
        x -= character.get_velocity()
        character.set_x(x)
                
        character.set_left(True)
        character.set_right(False)
        
        character.set_last_direction("left")
        
            
    elif keys[pygame.K_RIGHT]:
            
        x = character.get_x()
        x += character.get_velocity()
        character.set_x(x)
                
        character.set_left(False)
        character.set_right(True)
        
        character.set_last_direction("right")

    else:
        character.set_left(False)
        character.set_right(False)
        player_walk_count = 0
    
    if keys[pygame.K_SPACE]:
        if bullet.get_state() == "ready":
            direction = character.get_last_direction()
            bullet.set_x(character.get_x())
            bullet.set_y(character.get_y() + 10)
            
            shoot(bullet.get_x(), bullet.get_y())
        
    
    redraw_screen()
    




