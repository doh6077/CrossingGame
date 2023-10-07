from turtle import Turtle
MOVE_DISTANCE = 10
FINISH_LINE_Y = 275

class Player(Turtle):
    def __init__(self, shape, starting_position):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.color("black")
        self.starting_position = starting_position
        self.goto(starting_position)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(self.starting_position)


