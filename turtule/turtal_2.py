# draw a triangle, squre, pentagon, hexagon, heptagon, octagon, nonagon , decagon

import turtle
import random
t=turtle.Turtle()
sc=turtle.Screen()

arr=["green","blue","yellow","DarkMagenta",]
for a in range(8):
    max_round=a+3
    t.color(random.choice(arr))
    degree= 360/max_round
    for round in range(max_round):
        t.forward(100)
        t.right(degree)
    # t.right(degree)







sc.exitonclick()