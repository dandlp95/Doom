import pygame
import random
import math
from pygame import mixer
from player import Player
from bullet import Bullet
from enemy import Enemy

pygame.init()  # Start pygame

screen = pygame.display.set_mode((682, 512))  # Creates Screen

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
faces = ["../media/player/faces/doom-face1.png", "../media/player/faces/doom-face2.png", "../media/player/faces/doom-face3.png",
         "../media/player/faces/doom-face4.png", "../media/player/faces/doom-face5.png", "../media/player/faces/doom-face6.png",
         "../media/player/faces/doom-face7.png", "../media/player/faces/doom-face8.png", "../media/player/faces/doom-face9.png",
         "../media/player/faces/doom-face10.png", "../media/player/faces/doom-face11.png", "../media/player/faces/doom-face12.png",
         "../media/player/faces/dead.png"]

# Setting up character
character = Player()

character.set_x(20)
character.set_y(300)
character.set_velocity(5)
character.set_height(64)
character.set_width(64)
character.set_last_direction("left")
character.set_is_standing(True)
character.set_lives(10)

# Setting up enemy
enemy = Enemy()
enemy.set_x(690)
enemy.set_y(275)
enemy.set_velocity(5)

# Setting up projectiles
bullet = Bullet()

bullet.set_state("ready")
bullet.set_velocity(15)

fire_ball = Bullet()
fire_ball.set_state("ready")
fire_ball.set_velocity(15)
fire_ball.set_image("../media/enemy/fire-ball.png")

# Character moving
x = character.get_x()
y = character.get_y()

time_elapsed = 0
clock1 = pygame.time.Clock()

frame = 0


def is_collision(enemy_x, enemy_y, projectile_x, projectile_y, d):
    distance = math.sqrt(math.pow(enemy_x - projectile_x, 2) +
                         math.pow(enemy_y - projectile_y, 2))
    #print(enemy_x, enemy_y, projectile_x, projectile_y)
    if distance < d:
        return True
    else:
        return False


def shoot(x, y):
    bullet.set_state("fire")
    screen.blit(pygame.image.load(bullet.get_image()), (x, y))


def redraw_screen():

    # background.
    screen.blit(background, (0, 0))

    global player_walk_count
    global frame
    global direction
    global time_elapsed

    if frame + 1 >= 27:
        frame = 0

    if player_walk_count + 1 >= 27:
        player_walk_count = 0

    if character.get_lives() <= 0:
        face_img = faces[12]
        screen.blit(pygame.image.load(face_img), (20, 20))

    if character.get_left():
        walk_left_animation = character.get_walkLeft_animation()
        screen.blit(pygame.image.load(
            walk_left_animation[player_walk_count//3]), (character.get_x(), character.get_y()))
        player_walk_count += 1

        if character.get_lives() == 10:
            face = faces[2]
        elif character.get_lives() >= 8:
            face = faces[5]
        elif character.get_lives() >= 6:
            face = faces[8]
        elif character.get_lives() <= 5:
            face = faces[11]
        screen.blit(pygame.image.load(face), (20, 20))

    elif character.get_right():

        walk_right_animation = character.get_walkRight_animation()
        screen.blit(pygame.image.load(
            walk_right_animation[player_walk_count//3]), (character.get_x(), character.get_y()))
        player_walk_count += 1

        if character.get_lives() == 10:
            face = faces[1]
        elif character.get_lives() >= 8:
            face = faces[4]
        elif character.get_lives() >= 6:
            face = faces[7]
        elif character.get_lives() <= 5:
            face = faces[10]
        screen.blit(pygame.image.load(face), (20, 20))

    elif character.get_is_standing():
        if character.get_last_direction() == "left":
            doom_guy_img = character.get_image_l()
        elif character.get_last_direction() == "right":
            doom_guy_img = character.get_image_r()

        screen.blit(pygame.image.load(doom_guy_img),
                    (character.get_x(), character.get_y()))

        if character.get_lives() == 10:
            face = faces[0]
        elif character.get_lives() >= 8:
            face = faces[3]
        elif character.get_lives() >= 6:
            face = faces[6]
        elif character.get_lives() <= 5:
            face = faces[9]

        screen.blit(pygame.image.load(face), (20, 20))

    elif not character.get_is_standing():

        if character.get_is_shooting():

            if character.get_last_direction() == "left":
                doom_guy_img = character.get_img_shooting_l()

                if character.get_lives() == 10:
                    face_img = faces[2]
                elif character.get_lives() >= 8:
                    face_img = faces[5]
                elif character.get_lives() >= 6:
                    face_img = faces[8]
                elif character.get_lives() <= 5:
                    face_img = faces[11]

            elif character.get_last_direction() == "right":
                doom_guy_img = character.get_img_shooting_r()

                if character.get_lives() == 10:
                    face_img = faces[1]
                elif character.get_lives() >= 8:
                    face_img = faces[4]
                elif character.get_lives() >= 6:
                    face_img = faces[7]
                elif character.get_lives() <= 5:
                    face_img = faces[10]

            screen.blit(pygame.image.load(doom_guy_img),
                        (character.get_x(), character.get_y()))
            screen.blit(pygame.image.load(face_img), (20, 20))

        elif character.is_jump():
            doom_jumping = character.get_jump_img()

            if character.get_lives() == 10:
                face_img = faces[0]
            elif character.get_lives() >= 8:
                face_img = faces[3]
            elif character.get_lives() >= 6:
                face_img = faces[6]
            elif character.get_lives() <= 5:
                face_img = faces[9]

            screen.blit(pygame.image.load(doom_jumping),
                        (character.get_x(), character.get_y()))
            screen.blit(pygame.image.load(face_img), (20, 20))

    if enemy.get_x() < 10:
        enemy.set_last_direction("right")
    if enemy.get_x() > 675:
        enemy.set_last_direction("left")

    if enemy.get_is_attacking():

        if enemy.get_last_direction() == "left":
            attack_img = enemy.get_img_attack_l()
        else:
            attack_img = enemy.get_img_attack_r()

        screen.blit(pygame.image.load(attack_img),
                    (enemy.get_x(), enemy.get_y()))

    else:
        if enemy.get_last_direction() == "left":
            walk_animation = enemy.get_walkLeft_animation()
        else:
            walk_animation = enemy.get_walkRight_animation()
        screen.blit(pygame.image.load(
            walk_animation[frame//3]), (enemy.get_x(), enemy.get_y()))

        if enemy.get_last_direction() == "left":
            enemy.set_x(enemy.get_x() - enemy.get_velocity())
        else:
            enemy.set_x(enemy.get_x() + enemy.get_velocity())

    if fire_ball.get_state() == "fire":
        screen.blit(pygame.image.load(fire_ball.get_image()),
                    (fire_ball.get_x(), fire_ball.get_y()))

        if enemy.get_last_direction() == "left":
            fire_ball.set_x(fire_ball.get_x() - fire_ball.get_velocity())
        else:
            fire_ball.set_x(fire_ball.get_x() + fire_ball.get_velocity())

    if fire_ball.get_x() <= 0 or fire_ball.get_x() >= 682:
        fire_ball.set_x(enemy.get_x())
        fire_ball.set_state("ready")
        enemy.set_attack(False)
        time_elapsed = 0

    bullet_character_distance = abs(bullet.get_x() - character.get_x())
    if bullet_character_distance > 70:
        character.set_is_standing(True)
        character.set_is_shooting(False)

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

    dt = clock1.tick()
    time_elapsed += dt

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
            bullet.set_y(character.get_y() + 20)

            character.set_is_shooting(True)
            character.set_is_standing(False)

            shoot(bullet.get_x(), bullet.get_y())

    if character.is_jump() == False:
        if keys[pygame.K_UP]:
            character.set_jump(True)
            character.set_right(False)
            character.set_left(False)
            character.set_is_shooting(False)
            character.set_is_standing(False)
            player_walk_count = 0
    else:
        if character.get_jump_count() >= -8:
            neg = 1
            if character.get_jump_count() < 0:
                neg = -1
            character.set_y(character.get_y() -
                            (character.get_jump_count() ** 2) * 0.5 * neg)
            character.set_jump_count(character.get_jump_count() - 1)
        else:
            character.set_jump(False)
            character.set_is_standing(True)
            character.set_jump_count(8)

    if (700 <= time_elapsed) and enemy.get_is_attacking() == False:

        enemy.set_attack(True)
        fire_ball.set_x(enemy.get_x())
        fire_ball.set_y(enemy.get_y() + 20)
        fire_ball.set_state("fire")

    enemy_collision = is_collision(
        enemy.get_x(), enemy.get_y(), bullet.get_x(), bullet.get_y(), 50)
    if enemy_collision:
        print("You hit the enemy")

    character_collision = is_collision(
        character.get_x(), character.get_y(), fire_ball.get_x(), fire_ball.get_y(), 10)
    if character_collision:
        character.set_lives(character.get_lives() - 1)
        print("The enemy hit you")

    redraw_screen()
