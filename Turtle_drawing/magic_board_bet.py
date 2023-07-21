from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)

# Turtle races

# user_bet = screen.textinput(title = "Make your bet", prompt = "Place your bet! Which turtle wins? (rainbow colors): ")
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# starting_y = -70
# all_turtles = []
# is_race_on = False

# for turtle_index in range(0, 6):
#     new_turtle = Turtle("turtle")
#     new_turtle.penup()
#     new_turtle.color(colors[turtle_index])
#     new_turtle.goto(-230, starting_y)
#     starting_y += 40
#     all_turtles.append(new_turtle)

# if user_bet:
#     is_race_on = True

# while is_race_on:

#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"Your {winning_color} turtle won. Congratulations!")
#             else:
#                 print(f"You lose! The {winning_color} turtle was the winner")
#             break

#         random_distance = random.randint(0, 15)
#         turtle.forward(random_distance)



# Magic Board

# tim = Turtle()
# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def turn_left():
#     tim.left(10)

# def turn_right():
#     tim.right(10)

# def reset():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(move_forwards, "Up")
# screen.onkey(move_backwards, "Down")
# screen.onkey(turn_left, "Left")
# screen.onkey(turn_right, "Right")
# screen.onkey(reset, "c")






screen.exitonclick()