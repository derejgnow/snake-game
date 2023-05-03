from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.new_position()

    def new_position(self):
        food_x_coordinate = random.randrange(-280, 280, 20)
        food_y_coordinate = random.randrange(-280, 280, 20)
        self.goto(food_x_coordinate, food_y_coordinate)
