
import time
from turtle import Screen

from car import Car
from player import Player
from scoreboard import Scoreboard

PLAYER1_STARTING_POSITION = (-50, -280)
PLAYER2_STARTING_POSITION = (50, -280)

screen = Screen()
screen.setup(width=400, height=600)
screen.tracer(0)
screen.bgpic("cross2.png")
screen.update()

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

    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    for i in range(len(car.all_cars)):
        if car.all_cars[i].distance(player1) < 20:  # Adjust the distance threshold as needed
            player1.reset_position()

        if car.all_cars[i].distance(player2) < 20:  # Adjust the distance threshold as needed
            player2.reset_position()
