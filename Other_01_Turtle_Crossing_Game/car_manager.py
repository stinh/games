from turtle import Turtle
import random

COLORS = ["#b5179e", "#7209b7", "#560bad", "#480ca8", "#3a0ca3", "#4361ee", "#4895ef"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.random_y = random.randint(-240, 240)
        self.random_x = random.randint(-260, 500)
        self.setheading(180)
        self.goto(self.random_x, self.random_y)
        self.color(random.choice(COLORS))
        self.reset()

    def move(self, current_score):
        new_x = self.xcor() - (STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (current_score-1))
        self.goto(new_x, self.ycor())

    def reset(self):
        if self.xcor() < -350:
            self.goto(320, self.ycor())
