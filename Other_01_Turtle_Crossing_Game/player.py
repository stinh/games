from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("#0b4447")
        self.lt(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def goal(self):
        if self.ycor() > FINISH_LINE_Y:
            self.reset()
            return True

    def reset(self):
        self.goto(STARTING_POSITION)
