import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up") 

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    scoreboard.update_scoreboard()
    

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.reached_finish_line():
        player.reset_player()
        car_manager.increase_speed()
        scoreboard.increase_score()

screen.exitonclick()

"""Learnings
1. Forgot about exitonclick! Then all objects stop moving upon colliding
(instead of the screen closing). 
2. Don't touch the time.sleep func. Increment the backward in car_manager instead."""



