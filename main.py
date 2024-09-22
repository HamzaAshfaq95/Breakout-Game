from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard
import time

# CONSTANTS
# PADDLE INITIAL POSITION
PADDLE_X = 0
PADDLE_Y = -325
BALL_X = 0
BALL_Y = -298
game = True
yellow_blocks_1 = [(-450, 0), (-345, 0), (-240, 0), (-135, 0), (-30, 0), (75, 0), (180, 0), (285, 0), (390, 0), (495, 0)]
yellow_blocks_2 = [(-450, 25), (-345, 25), (-240, 25), (-135, 25), (-30, 25), (75, 25), (180, 25), (285, 25), (390, 25), (495, 25)]
green_blocks_1 = [(-450, 50), (-345, 50), (-240, 50), (-135, 50), (-30, 50), (75, 50), (180, 50), (285, 50), (390, 50), (495, 50)]
green_blocks_2 = [(-450, 75), (-345, 75), (-240, 75), (-135, 75), (-30, 75), (75, 75), (180, 75), (285, 75), (390, 75), (495, 75)]
orange_blocks_1 = [(-450, 100), (-345, 100), (-240, 100), (-135, 100), (-30, 100), (75, 100), (180, 100), (285, 100), (390, 100), (495, 100)]
orange_blocks_2 = [(-450, 125), (-345, 125), (-240, 125), (-135, 125), (-30, 125), (75, 125), (180, 125), (285, 125), (390, 125), (495, 125)]
red_blocks_1 = [(-450, 150), (-345, 150), (-240, 150), (-135, 150), (-30, 150), (75, 150), (180, 150), (285, 150), (390, 150), (495, 150)]
red_blocks_2 = [(-450, 175), (-345, 175), (-240, 175), (-135, 175), (-30, 175), (75, 175), (180, 175), (285, 175), (390, 175), (495, 175)]

# Screen Creation
screen = Screen()
# Screen Title
screen.title("Breakout")
# Screen Background Color
screen.bgcolor("Black")
# Screen Size
screen.setup(width=1000, height=750)
# tracer() will not show turtle moving (need to use update() to show the turtle)
screen.tracer(0)

# Paddle Creation
paddle = Paddle(PADDLE_X, PADDLE_Y)
# Paddle Movement
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

# Ball Creation
ball = Ball(BALL_X, BALL_Y)

# Blocks Creation
block_list_1 = []
block_list_2 = []
block_list_3 = []
block_list_4 = []
block_list_5 = []
block_list_6 = []
block_list_7 = []
block_list_8 = []
for position in yellow_blocks_1:
    block = Blocks(position, "yellow")
    block_list_1.append(block)
for position in yellow_blocks_2:
    block = Blocks(position, "yellow")
    block_list_2.append(block)
for position in green_blocks_1:
    block = Blocks(position, "green")
    block_list_3.append(block)
for position in green_blocks_2:
    block = Blocks(position, "green")
    block_list_4.append(block)
for position in orange_blocks_1:
    block = Blocks(position, "orange")
    block_list_5.append(block)
for position in orange_blocks_2:
    block = Blocks(position, "orange")
    block_list_6.append(block)
for position in red_blocks_1:
    block = Blocks(position, "red")
    block_list_7.append(block)
for position in red_blocks_2:
    block = Blocks(position, "red")
    block_list_8.append(block)

Scoreboard = Scoreboard()

def collision(list):
    for block in list:
        if block.distance(ball) < 40:
            block.goto(1000, 1000)
            ball.x_bounce()
            Scoreboard.point()

# update() will show the turtle
while game:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.y_bounce()
    if ball.distance(paddle) < 35:
        if ball.ycor() < -300:
            ball.x_bounce()
    if ball.ycor() > 355:
        ball.x_bounce()
    if ball.ycor() < -340:
        ball.goto(BALL_X, BALL_Y)
        paddle.goto(PADDLE_X, PADDLE_Y)
    collision(block_list_1)
    collision(block_list_2)
    collision(block_list_3)
    collision(block_list_4)
    collision(block_list_5)
    collision(block_list_6)
    collision(block_list_7)
    collision(block_list_8)
# Prohibit the screen to exit on click only
screen.exitonclick()