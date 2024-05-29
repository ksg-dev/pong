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


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

playing = True
while playing:
    screen.update()
    # Pause between movements so ball isn't as fast
    time.sleep(0.1)
    ball.move()

    # Detect collision w wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision w paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 375:
        ball.restart()

    # Detect if left paddle misses
    if ball.xcor() < -375:
        ball.restart()



screen.exitonclick()
