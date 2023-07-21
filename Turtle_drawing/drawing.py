import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# spirograph

# def draw_spirograph(size_of_gap):
#     tim.speed("fastest")
#     screen.bgcolor("black")    
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(7)


# Fantasy

# def draw_fantasy():
#     tim.speed(200)

#     screen.bgcolor("black")
#     for i in range(400):
#         tim.color(random_color())
#         tim.forward(50 + i)
#         tim.right(90.991)
    
#     tim.hideturtle()

# draw_fantasy()


# simple maze

# tim.speed(100)
# for i in range(200):
#     tim.forward(2+2*i)
#     tim.right(90)


# chess board

# def draw_square():
#     for i in range(4):
#         tim.forward(30)
#         tim.left(90)
#     tim.forward(30)

# def draw_half_board(start_y):
#     for i in range(4):
#         tim.up()
#         tim.setpos(-100, start_y + 30 * i)
#         tim.down()

#         for j in range(8):
#             if (i+j) % 2 == 0:
#                 col = "black"
#             else:
#                 col = "white"
            
#             tim.fillcolor(col)
#             tim.begin_fill()
#             draw_square()
#             tim.end_fill()

# def draw_board():
#     tim.speed(100)

#     draw_half_board(0)
#     draw_half_board(-120)
    
    
#     tim.hideturtle()

# draw_board()

screen.exitonclick()
