from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.color("white")
        self.shapesize(7, 1)
        self.right(90)
        self.penup()
        self.goto(self.x, self.y)

    def go_left(self):
        x = self.xcor() - 40
        if not self.xcor() == -420:
            self.goto(x, self.ycor())

    def go_right(self):
        x = self.xcor() + 40
        if not self.xcor() == 420:
            self.goto(x, self.ycor())