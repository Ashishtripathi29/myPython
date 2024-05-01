import turtle
t=turtle.Turtle()
sc=turtle.Screen()



def Move_forword():
    t.forward(10)
def Move_backword():
    t.backward(10)
def Move_left():
    newHeading=t.heading()+10
    t.setheading(newHeading)
def Move_right():
    newHeading=t.heading()-10
    t.setheading(newHeading)
def clear():
   
    t.reset()






sc.listen()
sc.onkey(Move_forword,"d")
sc.onkey(Move_backword,"a")
sc.onkey(Move_left,"w")
sc.onkey(Move_right,"s")
sc.onkey(clear,"c")

sc.exitonclick()