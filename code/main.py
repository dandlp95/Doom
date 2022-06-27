import pygame
import random
import math
from pygame  import mixer
from player import Player
from bullet import Bullet
from enemy import Enemy

pygame.init() # Start pygame

screen = pygame.display.set_mode((1400,600)) # Creates Screen

mixer.music.load("../media/Doom.wav")
mixer.music.play(-1)

# Title and Icon.
pygame.display.set_caption("Doom")
icon = pygame.image.load("../media/001-pentagram.png")
pygame.display.set_icon(icon)
background = pygame.image.load("../media/background2.jpg")


# Start game.
running = True

while running:
    # Needs to come first.
    screen.fill((0,0,0))
    
    # Hell background.
    screen.blit(background, (0,0))
    
    # Anything persistant goes inside this loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()




