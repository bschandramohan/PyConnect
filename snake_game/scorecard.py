from turtle import Turtle


class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("white")
        self.penup()
        self.goto(-40, 280)
        self.shape("blank")
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, font=("Arial", 14, "normal"))

    def increment(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(-40, 0)
        self.clear()
        self.color("red")
        self.write(f"Game Over! Final Score: {self.score}", False, font=("Arial", 16, "normal"))
