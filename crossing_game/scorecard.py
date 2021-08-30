from turtle import Turtle


class ScoreCard(Turtle):
    def __init__(self):
        super(ScoreCard, self).__init__()
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.hideturtle()

    def finish(self, success):
        self.clear()
        if success:
            self.write("SUCCESS!")
        else:
            self.write("Sorry! Game Over")
