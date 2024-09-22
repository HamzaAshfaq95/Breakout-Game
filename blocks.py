from turtle import Turtle

class Blocks(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 5)
        self.goto(position)
        self.color(color)