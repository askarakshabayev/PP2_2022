from random import randint
import pygame

screen = pygame.display.set_mode((400, 400))

background = pygame.Surface((400, 200))
background.fill((0, 255, 0))

xb = 0
yb = 100

surf = pygame.Surface((100, 100))
surf.fill((255, 0, 0))

x = 0
y = 50

background.blit(surf, (x, y))
screen.blit(background, (xb, yb))

pygame.display.update()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            yb = randint(0, 200)

    if x < 400:
        x += 2
    else:
        x = 0
    screen.fill((0, 0, 0))
    background.fill((0, 255, 0))
    background.blit(surf, (x, y))
    screen.blit(background, (xb, yb))
    pygame.display.update()

    pygame.time.delay(30)

pygame.quit()