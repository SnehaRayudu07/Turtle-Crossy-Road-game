import turtle
import random

# Game setup
window = turtle.Screen()
window.title("Crossy Road")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Player
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.setheading(90)  # Set turtle to face up
player.penup()
player.goto(0, -230)  # Adjust the y-coordinate as needed

# Player movement
def move_up():
    y = player.ycor()
    player.sety(y + 20)

def move_down():
    y = player.ycor()
    player.sety(y - 20)

def move_left():
    x = player.xcor()
    player.setx(x - 20)

def move_right():
    x = player.xcor()
    player.setx(x + 20)

# Keyboard bindings
window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# Car Manager
class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 1 # Adjust car speed as needed

    def create_car(self):
        random_chance = random.randint(1, 50)  # Lower probability for car generation
        if random_chance == 1:
            car = turtle.Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(colors))
            random_y = random.randint(-200, 200)  # Adjust the y-coordinate range as needed
            random_x = random.randint(800, 1000)  # Adjust the x-coordinate range as needed
            car.goto(random_x, random_y)

            # Check for overlapping cars
            is_overlapping = False
            for existing_car in self.all_cars:
                if car.distance(existing_car) < 40:
                    is_overlapping = True
                    break

            if not is_overlapping:
                self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

car_manager = CarManager()

# Obstacles (Cars)
colors = ["blue","yellow"]

# Goal
goal = turtle.Turtle()
goal.shape("turtle")
goal.color("green")
goal.setheading(270)  # Set turtle to face down
goal.penup()
goal.goto(0, 260)

# Game Over message
game_over_display = turtle.Turtle()
game_over_display.color("white")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)

def display_game_over():
    game_over_display.clear()
    game_over_display.write("Game Over", align="center", font=("Courier", 36, "normal"))

# Win message
win_display = turtle.Turtle()
win_display.color("white")
win_display.penup()
win_display.hideturtle()
win_display.goto(0, 0)

def display_win():
    win_display.clear()
    win_display.write("You Won!", align="center", font=("Courier", 36, "normal"))

# Collision detection
def check_collision():
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            return True
    return False

# Main game loop
while True:
    car_manager.create_car()
    car_manager.move_cars()

    if check_collision():
        display_game_over()
        break

    if player.distance(goal) < 20:
        display_win()
        break

    window.update()

# Run the game
window.mainloop()
