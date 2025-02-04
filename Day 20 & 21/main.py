from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True  

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.writeScore()
    if snake.head.distance(food) < 25: # detect collision
        food.refresh()
        scoreboard.updateScore() 
        scoreboard.writeScore()

screen.exitonclick()