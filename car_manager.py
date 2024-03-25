COLORS=["red","yellow","green","orange","pink","blue","purple"]
MOVE_INCREMENT=5
from turtle import Turtle
import random
class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.starting_move_distance=5
    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            car=Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            car.goto(300,random_y)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.starting_move_distance)

    def increase_speed(self):
        self.starting_move_distance+=MOVE_INCREMENT