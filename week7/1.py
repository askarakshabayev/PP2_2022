# pip install virtualenv
# python3 -m venv name_of_env
# source path_to_env/bin/activate
# pip install pygmae

import pygame

pygame.init()

size = width, height = (400, 300)

screen = pygame.display.set_mode(size)

screen.fill((255, 0, 0))  # black

pygame.draw.rect(screen, (0, 100, 10), (20, 30, 100, 100), 10)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

pygame.quit()

