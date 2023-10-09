import pygame

MOVE_DISTANCE = 10

class Player(pygame.sprite.Sprite):
    def __init__(self, starting_position, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = starting_position

    def go_up(self):
        self.rect.y -= MOVE_DISTANCE

    def go_down(self):
        self.rect.y += MOVE_DISTANCE

    def reset_position(self):
        self.rect.center = self.starting_position
