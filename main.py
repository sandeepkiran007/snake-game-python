from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("background.png")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
is_game_over = False
while not is_game_over:
    time.sleep(0.1)
    snake.move()
    screen.update()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increment_score()
        score_board.update_score()

    # detect collision with wall
    snake_xcor, snake_ycor = snake.head.pos()
    if snake_xcor > 280 or snake_ycor > 280 or snake_xcor < -290 or snake_ycor < -280:
        is_game_over = True
        score_board.game_over()

    # detech collision with tail
    for body in snake.body[1:]:
        if snake.head.distance(body) < 10:
            is_game_over = True
            score_board.game_over()


screen.exitonclick()
