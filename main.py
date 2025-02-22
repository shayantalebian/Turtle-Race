import turtle as Turtle_Module
import random as R

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-75, -45, -15, 15, 45, 75]
all_turtles = []
is_race_on = False

#SECTION - Screen setups
turtle_screen = Turtle_Module.Screen()
turtle_screen.setup(width=500, height=400)
turtle_screen.title("Turtle Race")

while True:
    try:
        user_bet = turtle_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
        if user_bet is None:  # If user cancels the input
            raise ValueError("You must enter a color to continue.")
        user_bet = user_bet.lower()
        if user_bet not in colors:
            raise ValueError("Invalid color. Please choose from red, orange, yellow, green, blue, or purple.")
        break 
    except ValueError as error:
        turtle_screen.textinput(title="Invalid Input", prompt=str(error) + "\nChoose OK and try again:")
if user_bet:
    is_race_on = True

#SECTION - Turtle setups

for turtle_index in range(0, 6):
    new_turtle = Turtle_Module.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You won! The {wining_color} turtle is the winner!")
            else:
                print(f"You lost! The {wining_color} turtle is the winner!")
            is_race_on = False
            break
        random_distance = R.randint(0, 10)
        turtle.forward(random_distance)

turtle_screen.exitonclick()
