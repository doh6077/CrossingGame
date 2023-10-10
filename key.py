import pygame

class Key(pygame.sprite.Sprite):
    def __init__(self, screen_width, y_position):
        super().__init__()
        self.image = pygame.image.load("key.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        self.rect.y = y_position
