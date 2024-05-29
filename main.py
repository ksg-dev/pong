from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("BATTLE PONG")
# this plus time/while loop below hides beginning animation
screen.tracer(0)


l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")

screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")

playing = True
while playing:
    screen.update()
    time.sleep(0.1)

    ball.start()


screen.exitonclick()
