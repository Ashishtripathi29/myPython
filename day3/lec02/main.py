print("welcom to the python game : ")
side=input(" now you have to home, you are at the junction \n would you like to go left or right ")

if(side=='left'):
    side=input('you come at position where is 3 way left right strait which side would you like to go')
    if(side=='left'):
        print('you can go your home')
        print('''                      (_)            
 _ __ _   _ _ __  _ __  _ _ __   __ _ 
| '__| | | | '_ \| '_ \| | '_ \ / _` |
| |  | |_| | | | | | | | | | | | (_| |
|_|   \__,_|_| |_|_| |_|_|_| |_|\__, |
                                 __/ |
                                |___/ ''')
    else:
        print('gaye bhad me ')
else:
    print('game over you have to go jail')