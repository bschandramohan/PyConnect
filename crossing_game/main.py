import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scorecard import ScoreCard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
car_manager.create_cars()

score_card = ScoreCard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.5)

    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 15:
            score_card.finish(success=False)
            game_on = False

    # Detect Success
    if player.ycor() == 280:
        score_card.finish(True)
        game_on = False

screen.exitonclick()
