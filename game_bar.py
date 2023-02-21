from turtle import Turtle


class GameBar(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.color("black")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_cor, 0)

    def move_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)

    def move_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)
