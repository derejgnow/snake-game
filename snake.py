from turtle import Turtle

STARTING_SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake = []
        for position in STARTING_SNAKE_POSITION:
            self.add_snake_part(position)
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def add_snake_part(self, position):
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.setposition(position)
        self.snake.append(snake_part)

    def turn_up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def turn_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def turn_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def turn_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def move(self):
        for part_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[part_num - 1].xcor()
            new_y = self.snake[part_num - 1].ycor()
            self.snake[part_num].setposition(new_x, new_y)

        self.snake[0].forward(20)

    def extend(self):
        self.add_snake_part(self.tail.pos())

    def snake_on_snake(self):
        snake_body = self.snake[1:]
        snake_eat_snake = False
        for space in snake_body:
            if self.head.distance(space) < 0.1:
                snake_eat_snake = True
        if snake_eat_snake:
            return True

