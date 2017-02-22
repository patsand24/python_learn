'''
Program that uses squares to draw a circle in python
'''

import turtle
window = turtle.Screen()
window.bgcolor("red")

def draw_square():
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("green")
    brad.speed(2)
    for i in range(0, 36):
        for x in range(0, 4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)

#def draw_circle():
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")

    #angie.circle(100)



draw_square()
#draw_circle()
window.exitonclick()
