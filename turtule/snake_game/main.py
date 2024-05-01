from turtle import  Screen 
from snake import Snake
from food import Food
from scorebourd import Scorebourd
# from sound import Create_sound

# sound=Create_sound("end.wav")
import pygame

def play_sound(sound_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

sound_file = "end.wav"  # Replace this with the path to your sound file




import time
sc=Screen()
sc.setup(600,600)
sc.bgcolor("black")
sc.title("My Snake game")

sc.tracer(0)

snake=Snake()

f=Food()
score=Scorebourd()



running = True
while running :
    sc.update()
    time.sleep(0.1)
    snake.move_snake()
    sc.listen()
    sc.onkey(snake.Move_left,"a")
    sc.onkey(snake.Move_right,"d")
    sc.onkey(snake.Move_up,"w")
    sc.onkey(snake.Move_down,"s")
    sc.onkey(snake.Move_left,"Left")
    sc.onkey(snake.Move_right,"Right")
    sc.onkey(snake.Move_up,"Up")
    sc.onkey(snake.Move_down,"Down")
    if(snake.head.distance(f)<15):
        f.create_new_food(score.get_score())
        snake.add_snake_bit()
        score.print_score()
    x=snake.head.xcor()
    y=snake.head.ycor()
    if(x>=290 or x<=-295 or y>=295 or y<=-290 or snake.is_snake_bite_itself()):
        play_sound(sound_file)
        score.end_game()
        running=False
    # if(snake.is_snake_bite_itself()):
    #     score.end_game()
    #     running=False

    

sc.exitonclick()