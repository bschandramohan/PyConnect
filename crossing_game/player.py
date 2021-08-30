from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        # self.shape("arrow")
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.setheading(90)
        self.goto(0, -280)
        self.speed("fastest")
        self.showturtle()

    def go_up(self):
        if self.ycor() < 280:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor() - 20)

    def go_right(self):
        if self.xcor() < 280:
            self.goto(self.xcor() + 20, self.ycor())

    def go_left(self):
        if self.xcor() > -280:
            self.goto(self.xcor() - 20, self.ycor())


