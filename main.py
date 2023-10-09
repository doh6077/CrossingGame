
import time
from turtle import Screen
import pygame

from car import Car
from player import Player, FINISH_LINE_Y
from scoreboard import Scoreboard
IMAGE ="car.gif"
PLAYER1_STARTING_POSITION = (-50, -280)
PLAYER2_STARTING_POSITION = (50, -280)
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Crossing Game")
car = Car()
scoreboard = Scoreboard()


# Create two player instances with different shapes and starting positions
player1 = Player("turtle", PLAYER1_STARTING_POSITION)
player2 = Player("triangle", PLAYER2_STARTING_POSITION)

screen.listen()
screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")

screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")

game_is_on = True
while game_is_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_on = False

        time.sleep(0.1)
        screen.update()

        car.create_car()
        car.move_cars()

        for i in range(len(car.all_cars)):
            if car.all_cars[i].distance(player1) < 20:
                player1.reset_position()

            if car.all_cars[i].distance(player2) < 20:
                player2.reset_position()

        if player1.ycor() > FINISH_LINE_Y and player2.ycor() > FINISH_LINE_Y:
            player1.reset_position()
            player2.reset_position()
            car.increaseSpeed()
            scoreboard.addscore()
            scoreboard.increase_level()

pygame.quit()