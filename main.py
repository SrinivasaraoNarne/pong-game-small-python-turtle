from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)

screen.listen()
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")
screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")

game_on = True

while game_on:
    time.sleep(ball.movement)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(paddle_r) < 20 or ball.distance(paddle_l) < 20:
        ball.hit()
    if ball.xcor() >= 330 or ball.xcor() <= -330:
        if ball.distance(paddle_r) < 50 or ball.distance(paddle_l) < 50:
            ball.hit()
    if ball.xcor() > 380:
        ball.reposition()
        score.pointl()
    if ball.xcor() < -380:
        ball.reposition()
        score.pointr()
    if score.r_score == 5 or score.l_score == 5:
        game_on = False

screen.exitonclick()
