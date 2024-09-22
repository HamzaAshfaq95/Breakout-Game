from turtle import Turtle

class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(self.x, self.y)
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.x_cor *= -1

    def x_bounce(self):
        self.y_cor *= -1