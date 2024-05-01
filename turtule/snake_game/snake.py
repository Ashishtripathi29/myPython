from turtle import Turtle 
starting_postion=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        self.head.shape("circle")
    
    def create_snake(self):
        for position in starting_postion:
            t=Turtle("square")
            # t.shapesize(0.6,)
            t.penup()
            t.goto(position)
            t.color("white")
            # t.shape("square")
            self.segments.append(t)
        

    def move_snake(self):
            for seg_num in range(len(self.segments)-1,0,-1):
                newX= self.segments[seg_num-1].xcor()
                newY=self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(newX,newY)
            self.head.forward(10)

    def add_snake_bit(self):
            t=Turtle("square")
            t.penup()
            x=self.segments[-1].xcor()
            y=self.segments[-1].ycor()
            t.goto(x,y)
            t.color("white")
            # t.shape("square")
            self.segments.append(t)
    
    def is_snake_bite_itself(self):
        snake_bite=False
        for i in  range(1,len(self.segments)):
             if (self.head.distance(self.segments[i])<5):
                  snake_bite=True
        return snake_bite
                  
              
         


    def Move_left(self):
        newHeading=self.head.heading()
        if(newHeading !=0.0):
            self.head.setheading(180.0)

    def Move_right(self):
        newHeading=self.head.heading()
        if(newHeading !=180.0):
            self.head.setheading(0.0)
    def Move_up(self):
        newHeading=self.head.heading()
        if(newHeading !=270.0):
            self.head.setheading(90.0)
    def Move_down(self):
        newHeading=self.head.heading()
        if(newHeading !=90.0):
            self.head.setheading(270.0)
    
    

        

