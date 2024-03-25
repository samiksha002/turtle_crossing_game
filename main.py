import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen=Screen()
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.setup(width=600,height=600)
screen.tracer(0)
player=Player()
screen.listen()
screen.onkey(player.move_up,"Up")
cars=CarManager()
score=Scoreboard()
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()
    for car in cars.all_cars:
        if car.distance(player)<20:
            score.game_over()
            game_is_on=False
    if player.ycor()>=280:
        player.refresh()
        score.increase_level()
        cars.increase_speed()
screen.exitonclick()