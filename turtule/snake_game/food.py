from turtle import Turtle
from random import randint




class Food(Turtle):

    def __init__(self) -> None:
            super().__init__()
            self.shape("circle")
            self.penup()
            self.speed("fastest")
            self.create_new_food(0)
            

    def create_new_food(self,s):
        if(s%5==0 and s!=0 and s%10!=0):
            self.color("yellow")
            self.shapesize(0.7,0.7)
        else:
            self.color("blue")
            self.shapesize(0.5,0.5)
        x =randint(-280,280)
        y=randint(-280,280)
        self.goto(x,y)
        
      