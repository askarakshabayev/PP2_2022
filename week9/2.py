from random import randint

import pygame

pygame.init()

pygame.time.set_timer(pygame.USEREVENT, 3000)

W = 400
H = 400

WHITE = (255, 255, 255)
CARS = ('car1.png', 'car2.png', 'car3.png')

CARS_SURF = []

sc = pygame.display.set_mode((W, H))

for i in range(len(CARS)):
    CARS_SURF.append(pygame.image.load(CARS[i]))


class Car(pygame.sprite.Sprite):
    def __init__(self, x, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.add(group)
        self.speed = randint(1, 3)

    def update(self):
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            self.kill()


cars = pygame.sprite.Group()

Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.USEREVENT:
            Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
    sc.fill(WHITE)

    cars.draw(sc)
    pygame.display.update()
    pygame.time.delay(20)

    cars.update()

pygame.quit()
