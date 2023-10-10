import pygame

ALIGNMENT = "center"

class Scoreboard(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 0
        with open("score.txt") as data:
            self.high_score = int(data.read())
        self.font = pygame.font.Font(None, 30)
        self.color = (0, 0, 0)
        self.update_scoreboard()

    def update_scoreboard(self):
        score_text = f"Score: {self.score} High Score: {self.high_score}"
        self.image = self.font.render(score_text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 10)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def addscore(self):
        self.score += 1
        self.increase_level()
