from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start):
        super().__init__()
        self.shape("square")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(start)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)







