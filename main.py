import random
import pygame
from car import Car
from key import Key
from player import Player
from scoreboard import Scoreboard

# Constants
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
FINISH_LINE_Y = 20
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Crossing Game")
clock = pygame.time.Clock()

# Load background image
background = pygame.image.load("background.png")

# Initialize players, cars, and scoreboard
player1 = Player((SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 60), "woodstock.png")
player1.image.set_colorkey((255, 255, 255))
player2 = Player((SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 60), "snoopy.png")
player2.image.set_colorkey((0, 0, 0))

key1 = Key(SCREEN_WIDTH // 2 - 50, 20)
key2 = Key(SCREEN_WIDTH // 2 + 50, 20)
key_group = pygame.sprite.Group()
key_group.add(key1, key2)

all_cars = pygame.sprite.Group()

scoreboard = Scoreboard()

player1_has_key = False
player2_has_key = False


# Function to create cars randomly
def create_car():
    if not player1_has_key or not player2_has_key:
        # Generate cars only if neither player has the key
        if scoreboard.level < 5:
            random_chance = random.randint(1, 6)
        elif scoreboard.level < 10:
            random_chance = random.randint(1, 4)
        else:
            random_chance = random.randint(1, 3)

        if random_chance == 1:
            car = Car(SCREEN_WIDTH)
            all_cars.add(car)



# Main game loop
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
            elif event.key == 119:
                player2.go_up()
            elif event.key == pygame.K_s:
                player2.go_down()

    player1.update()
    player2.update()
    key1.update()
    key2.update()
    create_car()
    for car in all_cars:
        car.move()

    # Check if either player reaches the finish line
    if player1.rect.y <= FINISH_LINE_Y and player2.rect.y <= FINISH_LINE_Y:
        player1.reset_position()
        player2.reset_position()
        scoreboard.increase_level()
        scoreboard.addscore()
        player1_has_key = False
        player2_has_key = False
        for car in all_cars:
            car.increase_speed()

    # Check for collisions with cars
    collided_with_cars = pygame.sprite.spritecollide(player1, all_cars, False) or pygame.sprite.spritecollide(player2, all_cars, False)

    # Check if there was a collision with cars and display "Game Over" text
    if collided_with_cars:
        scoreboard.update_scoreboard()
        scoreboard.reset()
        player1.reset_position()
        player2.reset_position()


    # Check for collisions with keys
    if pygame.sprite.spritecollide(player1, key_group, False):
        player1_has_key = True
    if pygame.sprite.spritecollide(player2, key_group, False):
        player2_has_key = True

    if player1_has_key or player2_has_key:
        all_cars.empty()

    # Draw everything on the screen
    screen.blit(background, (0, 0))
    screen.blit(player1.image, player1.rect)
    screen.blit(player2.image, player2.rect)
    screen.blit(key1.image, key1.rect)
    screen.blit(key2.image, key2.rect)
    screen.blit(scoreboard.image, scoreboard.rect)
    all_cars.draw(screen)

    # Update the scoreboard
    scoreboard.update_scoreboard()

    pygame.display.update()
    clock.tick(5)

pygame.quit()


