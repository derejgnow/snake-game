from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
from gameover import GameOver


my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.tracer(0)
my_screen.title("Snake Game")
my_screen.listen()


snake = Snake()


continue_game = True

food = Food()
scoreboard = Scoreboard()

while continue_game:
    my_screen.update()
    time.sleep(.075)

    snake.move()
    my_screen.onkey(fun=snake.turn_right, key="Right")
    my_screen.onkey(fun=snake.turn_left, key="Left")
    my_screen.onkey(fun=snake.turn_up, key="Up")
    my_screen.onkey(fun=snake.turn_down, key="Down")

    if snake.snake[0].distance(food) < 10:
        food.new_position()
        scoreboard.increase_score()
        snake.extend()

# Detecting snake eating itself
    if snake.snake_on_snake():
        continue_game = False
        gameover = GameOver()
    else:
        # Detecting snake colliding with wall
        if snake.head.xcor() > 290:
            continue_game = False
            gameover = GameOver()
        if snake.head.xcor() < -290:
            continue_game = False
            gameover = GameOver()
        if snake.head.ycor() > 290:
            continue_game = False
            gameover = GameOver()
        if snake.head.ycor() < -290:
            continue_game = False
            gameover = GameOver()

with open("data.txt", mode='r') as high_score_file_r:
    if scoreboard.score > int(high_score_file_r.read()):
        with open("data.txt", mode='w') as high_score_file_w:
            high_score_file_w.write(str(scoreboard.score))


my_screen.exitonclick()
