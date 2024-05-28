from turtle import Screen, Turtle
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("BATTLE PONG")
screen.tracer(0)
# screen.mode("logo")

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")

screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")

playing = True
while playing:
    screen.update()
    time.sleep(0.1)


print(paddle.shapesize())
screen.exitonclick()
