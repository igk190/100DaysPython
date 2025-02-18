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

screen.listen()
screen.onkey(player.move_up, "Up") 

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            print("Crash!")
            game_is_on = False

    if player.reached_finish_line():
        player.reset_player()
        car_manager.increase_speed()

screen.exitonclick()

"""Learnings
1. Forgot about exitonclick! Then all objects stop moving upon colliding
(instead of the screen closing). 
2. Don't touch the time.sleep func. Increment the backward in car_manager instead."""


"""Create a scoreboard that keeps track of 
which level the user is on. Every time the turtle player
 does a successful crossing, the level should increase. 
 When the turtle hits a car, GAME OVER should be displayed in
   the centre. Step 7.
"""


