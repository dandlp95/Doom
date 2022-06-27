import pygame
import random
import math
from pygame  import mixer
from player import Player
from bullet import Bullet
from enemy import Enemy

pygame.init() # Start pygame

screen = pygame.display.set_mode((682,512)) # Creates Screen

mixer.music.load("../media/Doom.wav")
mixer.music.play(-1)

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

left = False
# Character moving

x = character.get_x()
y = character.get_y()

frame = 0

def redraw_screen():
    
    # background.
    screen.blit(background, (0,0))
    
    global player_walk_count
    global frame
    
    # if frame + 1 >= 27:
    #     frame = 0
        
    # screen.blit(pygame.image.load(faces[frame//3]), (20, 20))
    
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
        screen.blit(pygame.image.load(character.get_image()), (x,y))
        screen.blit(pygame.image.load(faces[0]), (20, 20))
    
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
            
    elif keys[pygame.K_RIGHT]:
            
        x = character.get_x()
        x += character.get_velocity()
        character.set_x(x)
                
        character.set_left(False)
        character.set_right(True)

    else:
        character.set_left(False)
        character.set_right(False)
        player_walk_count = 0
    
    redraw_screen()
    




