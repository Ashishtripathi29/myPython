import turtle 
tim=turtle.Turtle()
sc=turtle.Screen()



# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

for a in range(40):
        tim.penup()
        for _ in range(1):
            if a%2==0:
                tim.left(90)
                tim.color("blue")
                tim.forward(10)
                tim.left(90)
            else:
                    tim.right(90)
                    tim.color("red")
                    tim.forward(10)
                    tim.right(90)
                  
            for _ in range(20):
                    tim.pendown()
                    tim.forward(10)
                    tim.penup()
                    tim.forward(10)




sc.exitonclick()

