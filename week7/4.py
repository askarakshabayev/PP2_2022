'''
if event.type == pygame.MOUSEBUTTONDOWN:
    event.dict['pos']
'''
import random

import pygame

pygame.init()

# RGB (255, 255, 255
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
C = (100, 100, 100)

size = width, height = (700, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('PyGame Rectangle example')

clock = pygame.time.Clock()  # FPS

colors = [WHITE, BLUE, GREEN, RED]

color = WHITE

x = 100
y = 100
dx = 1
dy = 0

speed = 1

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            dx = 0
            dy = -1 * speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            dx = 0
            dy = 1 * speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            dx = -1 * speed
            dy = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            dx = 1 * speed
            dy = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed += 3


    screen.fill(BLACK)
    x += dx
    y += dy

    if x > width:
        x = 0
    if x < 0:
        x = width
    if y > height:
        y = 0
    if y < 0:
        y = height

    pygame.draw.ellipse(screen, color, [x, y, 20, 20])
    clock.tick(30)
    pygame.display.update()

