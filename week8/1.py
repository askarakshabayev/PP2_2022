import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
surf = pygame.Surface((150, 150))

surf.fill((100, 150, 0))

pygame.draw.rect(surf, (10, 150, 200), (10, 10, 20, 20))
pygame.draw.rect(surf, (10, 150, 200), (30, 30, 20, 20))

done = False
x = 50
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            x += 3

    screen.fill((255, 255, 255))
    screen.blit(surf, (x, 20))
    pygame.display.flip()

pygame.quit()
