import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#ced4da")
screen.title("Turtle Crossing")
screen.tracer(0)
score = 1

# Create player turtle, and make the game screen listen to the up key.
player = Player()
screen.listen()
screen.onkeypress(key="Up", fun=player.move)

# Create a scoreboard on top right
scoreboard = Scoreboard()
cars = []


# Generate cars, increase moving speed every level
def car_manager():
    for n in range(20):
        new_car = CarManager()
        cars.append(new_car)


car_manager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_score(score)

    # Detect collision with the car, if a car hit the player, game is over; if not, cars move forward
    for car in cars:
        if car.distance(player) < 20:
            game_is_on = False
        else:
            car.move(score)
            car.reset()

    if player.goal():
        score += 1

scoreboard.game_over()
screen.exitonclick()
