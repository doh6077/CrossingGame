
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.score = 0
        with open("score.txt") as data:
            self.high_level = int(data.read())
        self.color("black")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.level} High Score: {self.high_level}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.level > self.high_level:
            self.high_level = self.level
            with open("score.txt", mode="w") as file:
                file.write(f"{self.high_level}")
        self.level = 0
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def addscore(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()