import random

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))


class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]  # [[x0, y0], [x1, y1], [x2, y2] ...] (i) -> (i - 1)
        self.radius = 10
        self.dx = 5  # Right.
        self.dy = 0
        self.is_add = False
        self.speed = 30

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 3 == 0:
            self.speed += 10

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx <= x <= foodx + 10 and foody <= y <= foody + 10:
            return True
        return False


class Food:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 800)

    def gen(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 800)

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10, 10))


snake1 = Snake(100, 100)
snake2 = Snake(150, 100)
food = Food()

running = True

FPS = 30
d = 5

clock = pygame.time.Clock()

while running:
    clock.tick(snake1.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # if event.key == pygame.K_SPACE:
            #     snake1.is_add = True
            #     snake2.is_add = True
            if event.key == pygame.K_RIGHT and snake1.dx != -d:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d

            if event.key == pygame.K_d:
                snake2.dx = d
                snake2.dy = 0
            if event.key == pygame.K_a:
                snake2.dx = -d
                snake2.dy = 0
            if event.key == pygame.K_w:
                snake2.dx = 0
                snake2.dy = -d
            if event.key == pygame.K_s:
                snake2.dx = 0
                snake2.dy = d

    if snake1.eat(food.x, food.y):
        snake1.is_add = True
        food.gen()

    if snake2.eat(food.x, food.y):
        snake2.is_add = True
        food.gen()

    snake1.move()
    snake2.move()
    screen.fill((0, 0, 0))
    snake1.draw()
    snake2.draw()
    food.draw()
    pygame.display.flip()

pygame.quit()
