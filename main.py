import random
import pygame
import sys
from car import Car
from player import Player

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
FINISH_LINE_Y = 275
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Crossing Game")
clock = pygame.time.Clock()

background = pygame.image.load("background.png")

player1 = Player((SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 60), "woodstock.png")
player1.image.set_colorkey((255, 255, 255))
player2 = Player((SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 60), "snoopy.png")
player2.image.set_colorkey((0, 0, 0))

all_cars = pygame.sprite.Group()

def create_car():
    random_chance = random.randint(1, 20)
    if random_chance == 1:
        car = Car(SCREEN_WIDTH)
        all_cars.add(car)

game_is_on = True
while game_is_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1.go_up()
            elif event.key == pygame.K_DOWN:
                player1.go_down()
            elif event.key == pygame.K_w:
                player2.go_up()
            elif event.key == pygame.K_s:
                player2.go_down()

    # Update player and car positions
    player1.update()
    player2.update()
    create_car()
    for car in all_cars:
        car.move()

    if player1.rect.y <= FINISH_LINE_Y and player2.rect.y <= FINISH_LINE_Y:
        player1.reset_position()
        player2.reset_position()

    if pygame.sprite.spritecollide(player1, all_cars, False) or pygame.sprite.spritecollide(player2, all_cars, False):
        game_is_on = False

    screen.blit(background, (0, 0))
    screen.blit(player1.image, player1.rect)
    screen.blit(player2.image, player2.rect)
    all_cars.draw(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
