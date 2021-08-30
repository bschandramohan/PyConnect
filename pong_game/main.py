from turtle import Screen
from pong_game.paddle import Paddle
from pong_game.ball import Ball
from pong_game.scorecard import ScoreCard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")

left_paddle = Paddle("LEFT")
right_paddle = Paddle("RIGHT")

ball = Ball()
score_card = ScoreCard()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_on = True
while game_on:
    ball.move()

    # Detect collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(right_paddle) < 30 and ball.xcor() > 320) or \
            (ball.distance(left_paddle) < 30 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect collision with side wall
    if ball.xcor() > 380:
        score_card.increment_left_score()
        ball.reset()
    elif ball.xcor() < -380:
        score_card.increment_right_score()
        ball.reset()

screen.exitonclick()
