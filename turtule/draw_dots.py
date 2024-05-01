import turtle
import random
import colorgram


colors = colorgram.extract('image.png', 50)
# print(colors)
color_arr=[]
for i in colors:
    # print(i.rgb)
    r=i.rgb.r
    g=i.rgb.g
    b=i.rgb.b
    color_arr.append((r,g,b))

# print(color_arr)

color_arr=[ (30, 249, 244), (254, 253, 37), (2, 36, 247), (3, 212, 9), (211, 3, 194), (247, 25, 4), (218, 239, 229), (222, 232, 246), (245, 214, 243), (251, 7, 0), (68, 227, 73), (53, 84, 252), (223, 16, 205), (252, 70, 51), (233, 120, 224), (227, 66, 214), (249, 116, 102), (246, 158, 148), (152, 167, 246), (112, 134, 248)]

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    co= (r,g,b)
    # print(co)
    return co



t=turtle.Turtle()
def print_dots(dots):
    turtle.colormode(255)
    t.penup()
    t.hideturtle()
    t.speed("fastest")
    t.setheading(225)
    t.forward(200)

    t.setheading(0)
    for i in range(1,dots+1):
        t.dot(10,random.choice(color_arr))
        t.forward(30)
        if(i%10==0):
            t.setheading(90)
            t.forward(30)
            t.setheading(180)
            t.forward(300)
            t.setheading(0)


print_dots()




sc=turtle.Screen()
sc.exitonclick()