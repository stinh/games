from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)

    def update_score(self, current_score):
        self.clear()
        self.write(f"Level: {current_score}", font=FONT)

    def game_over(self):
        self.color("#ff595e")
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
