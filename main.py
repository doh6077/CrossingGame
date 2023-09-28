
import time
from turtle import Screen
from player import Player

PLAYER1_STARTING_POSITION = (-50, -280)
PLAYER2_STARTING_POSITION = (50, -280)

screen = Screen()
screen.setup(width=400, height=600)
screen.tracer(0)
screen.bgpic("cross2.png")
screen.update()


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