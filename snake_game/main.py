from turtle import Screen
from snake_game.snake import Snake
from snake_game.food import Food
from snake_game.scorecard import ScoreCard

import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
score_card = ScoreCard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect collision with Food
    if snake.head.distance(food) < 15:
        food.position()
        score_card.increment()
        snake.extend()

    # Detect collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_card.game_over()
        game_on = False

    # Detect collision with tail
    for box in snake.boxes[2:]:
        if snake.head.distance(box) < 15:
            score_card.game_over()
            game_on = False

screen.exitonclick()
