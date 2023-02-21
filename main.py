from turtle import Screen
from game_bar import GameBar
from ball import Ball
import time
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("white")
my_screen.title("PING PONG")
my_screen.tracer(0)

r_bar = GameBar(350)
l_bar = GameBar(-350)
my_ball = Ball()
my_scoreboard = ScoreBoard()

my_screen.listen()

my_screen.onkeypress(r_bar.move_up, "Up")
my_screen.onkeypress(r_bar.move_down, "Down")
my_screen.onkeypress(l_bar.move_up, "w")
my_screen.onkeypress(l_bar.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(my_ball.move_speed)
    my_screen.update()
    my_ball.move()

    # to detect collision with wall
    if my_ball.ycor() > 270 or my_ball.ycor() < -270:
        my_ball.bounce_y()

    # detect collision with paddle

    if my_ball.distance(r_bar) < 50 and my_ball.xcor() > 320 or my_ball.distance(l_bar) < 50 and my_ball.xcor() < -320:
        my_ball.bounce_x()

    # detect if R player misses to hit the ball
    if my_ball.xcor() > 380:
        my_ball.reset_ball()
        my_scoreboard.l_point()

    # detect if L player misses to hit the ball
    if my_ball.xcor() < -380:
        my_ball.reset_ball()
        my_scoreboard.r_point()
my_screen.exitonclick()
