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

size = (700, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('PyGame Rectangle example')

clock = pygame.time.Clock()  # FPS

colors = [WHITE, BLUE, GREEN, RED]

rect_x = 50
rect_y = 50
rect_change_x = 2
rect_change_y = 2

color = WHITE
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color = colors[random.randint(0, 3)]
    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    screen.fill(BLACK)
    pygame.draw.rect(screen, color, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])

    clock.tick(60)  # 60 FPS
    pygame.display.update()

pygame.quit()
