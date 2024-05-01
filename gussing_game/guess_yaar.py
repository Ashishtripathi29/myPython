from random import randint

from art import logo




def setdifficulty():
    level=input("set you level, enter Easy, Medium, Hard: ")
    if(level== "easy" or level=="Easy"):
        return 10
    elif(level=="medium" or level=="Medium"):
        return 7
    elif(level=="Hard" or level=="hard"):
        return 5
    else:
        return "sorry!!!  please enter valid key..."
    

def guessNumber(user_number,ans,turm):
    if(user_number>ans):
        print("your guessing number is Higher then Answer")  
        return turm-1
    elif user_number<ans:
        print("your guessing number is Lower then Answer")  
        return turm-1
    else:
        print(f"The answer is {ans}")
        print("wow😍😍😁😁😀!! you won the Match")
        

    
def retry():
     retry=input("would you like to play again.. Y/N: ")
     if(retry=="Y" or "y"):
         game()
     else:
         return False




def game():
    print(logo)
    turm=setdifficulty()
    if type(turm)  is not  int:
        print(turm)
        turm=setdifficulty()
    ans=randint(1,100)
    
    while(turm>0):
        print(f"you have {turm} attempt..")
        user_number=int(input("Enter your Number: "))
        turm=guessNumber(user_number,ans,turm)
        if(ans!=user_number and turm>0):
            print("try again...")
        else:
            if(turm==0):
                print(f"The answer is {ans}")
                print("so sad!!!😥😥😥😥    you lose the game")
            run=retry()
            if(not run):break


game()