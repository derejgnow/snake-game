from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write(arg="Game Over.", align="Center", font=("Arial", 15, "normal"))
