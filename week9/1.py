from random import randint

import pygame

pygame.init()
W = 400
H = 400
WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, 0))

    def update(self):
        if self.rect.y < H:
            self.rect.y += 2
        else:
            self.rect.y = 0


sc = pygame.display.set_mode((W, H))

cars = pygame.sprite.Group()

car1 = Car(randint(1, W), 'car1.png')
car2 = Car(randint(1, W), 'car2.png')
car3 = Car(randint(1, W), 'car3.png')

cars.add(car1)
cars.add(car2)
cars.add(car3)

# update
# draw

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    sc.fill(WHITE)
    cars.draw(sc)
    pygame.display.update()
    pygame.time.delay(20)

    cars.update()
pygame.quit()
