import turtle
import random
sc = turtle.Screen()

turtle_colors = [
    "green",
    "blue",
    "yellow",
    "red",
    "orange",
    "purple",
    "brown",
    "pink",
    "cyan",
    "magenta",
    "teal",
    "lavender",
    "peach",
    "turquoise",
    "maroon",
    "gold",
    "silver",
    "navy",
    "indigo",
    "olive",
    "sky blue",
    "salmon",
    "lime",
    "violet",
    "tan",
    "auburn",
    "plum",
    "coral",
    "orchid",
    "steel blue",
    "khaki",
    "crimson",
    "periwinkle",
    "chartreuse",
    "sapphire",
    "rose",
    "ivory",
    "azure",
    "mint",
    "ruby",
    "emerald",
    "amber",
    "tangerine",
    "fuchsia",
    "copper",
    "rust",
    "lemon",
    "cerulean",
    "beige",
    "jade",
]



def run_game(n, player):
    players = []
    t = 1
    c = 0
    for i in range(n):
        if t == 1:
            t = -1
            c = 0
        else:
            c = 20
            t = 1
        new_turtal = turtle.Turtle()
        new_turtal.penup()
        new_turtal.color(turtle_colors[i])
        new_turtal.shape("turtle")
        new_turtal.goto(-380, i * 20 * t + c)
        players.append(new_turtal)
    max_range = False
    while not max_range:

        for tur in players:
            path = random.randint(0, 10)
            tur.forward(path)
            if tur.pos()[0] >= 380:
                max_range = True
                tur.goto(-100,280)
                if tur.pencolor() == player:
                    print(f"wow!!! you won the match, {tur.pencolor()} win...")
                    
                    tur.write(f"wow!!! you won the match, {tur.pencolor()} win...",font=("Arial", 16, "normal"))
                else:
                    print(f" you loss the match, {tur.pencolor()} win...")
                    tur.write(f" you loss the match, {tur.pencolor()} win...",font=("Arial", 16, "normal"))
                break
    # sc.reset()
    play_again=sc.textinput("play again?","yes/no")
    if(play_again=="yes"):
        start_game()







def start_game():
    sc.setup(800, 600)
    sc.listen()
    sc.clear()
    number_of_player = int(sc.textinput(
        "number of players", "enter the number of player min 2, maximum 10"
    ))
    while number_of_player>10 or number_of_player<2:
        number_of_player = int(
            sc.textinput("number of players", "enter the number of player maximum 10")
        )

    selected_color = turtle_colors[:number_of_player]
    name = sc.textinput(
        "player", f"{selected_color} select the one color in this for your players"
    )
    while not name in selected_color:
        name = sc.textinput(
            "player", f"{selected_color} select the one color in this for your players"
        )
    run_game(number_of_player, name)

start_game()

sc.exitonclick()
