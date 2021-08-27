from turtle import Turtle

RIGHT = 0
LEFT = 180
DOWN = 270
UP = 90
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0),
                      (-100, 0), (-120, 0), (-140, 0), (-160, 0), (-180, 0),
                      (-200, 0), (-220, 0), (-240, 0), (-260, 0), (-280, 0)]


class Snake:

    def __init__(self):
        self.boxes = []
        self.create_snake()
        self.head = self.boxes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_box = Turtle("square")
            new_box.color("white")
            new_box.penup()
            new_box.goto(position)
            self.boxes.append(new_box)

    def move(self):
        for step in range(len(self.boxes) - 1, 0, -1):
            previous_x = self.boxes[step - 1].xcor()
            previous_y = self.boxes[step - 1].ycor()
            self.boxes[step].goto(previous_x, previous_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        new_box = Turtle("square")
        new_box.color("white")
        new_box.penup()
        new_box.goto(self.boxes[-1].xcor(), self.boxes[-1].ycor())
        self.boxes.append(new_box)
