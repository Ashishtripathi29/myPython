import turtle
import random

t=turtle.Turtle()
sc=turtle.Screen()
turtle.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    co= (r,g,b)
    print(co)
    return co

def draw_spirograph(size_of_gap):
    t.speed("fastest")
    for _ in range(int(360/size_of_gap)+1):
        t.color(random_color())
        t.circle(100)
        t.setheading(size_of_gap*_)

draw_spirograph(15)
sc.exitonclick()

