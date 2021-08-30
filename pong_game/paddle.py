from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, init_side):
        super().__init__()
        self.init_side = init_side
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")

        if init_side == "LEFT":
            self.goto(-380, 0)
        else:
            self.goto(380, 0)

    def go_up(self):
        if self.ycor() < 240:
            self.clear()
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -240:
            self.clear()
            self.goto(self.xcor(), self.ycor() - 20)
