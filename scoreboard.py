from turtle import Turtle


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt", mode='r') as high_score_file_r:
            self.write(arg=f"Score: {self.score}, High Score: {int(high_score_file_r.read())}", align="Center",
                       font=("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        with open("data.txt", mode='r') as high_score_file_r:
            self.write(arg=f"Score: {self.score}, High Score: {int(high_score_file_r.read())}", align="Center",
                       font=("Courier", 15, "normal"))
