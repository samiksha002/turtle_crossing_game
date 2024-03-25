from turtle import Turtle
STARTING_POSITION=(0,-270)
MOVE_DISTANCE=10
FINISH_LINE_Y=280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(0,-270)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)
