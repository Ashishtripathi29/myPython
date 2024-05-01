from turtle import Turtle


class Scorebourd(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0,280)
        self.print_score()
       
    def print_score(self):
        self.clear()
        self.write(f"score: {self.score }",align="center",font=("Arial", 15, "normal"))
        if(self.score%5==0 and self.score!=0 and self.score%10!=0):self.score+=5
        else:self.score+=1
    def end_game(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Arial", 15, "normal"))

       
    
    def get_score(self):
        return self.score
