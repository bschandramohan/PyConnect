from turtle import Turtle
from random import Random


class Car(Turtle):

    valid_colors = ["red", "yellow", "blue", "green", "pink", "orange", "crimson"]

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.color(self.valid_colors[Random().randint(0, len(self.valid_colors) - 1)])
        self.penup()
        self.speed("fastest")
        random_position = Random().randint(-240, 290)
        random_position -= random_position % 20
        self.goto(378, random_position)

    def move(self):
        self.goto(self.xcor() - 25, self.ycor())
