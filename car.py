import pygame
import random

STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 10

class Car(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = pygame.image.load("car.png")
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        self.rect.y = random.randint(50, 430)
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.rect.x -= self.speed

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def decrease_speed(self):
        self.speed -= MOVE_INCREMENT