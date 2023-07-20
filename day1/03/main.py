print("welcome in the python cource")
print("Enter bellow deteils for voter id\n")
name=input("Enter your name:\n")
age=input("Enter your age:\n")
add=input("Enter your full address:\n")
adhar=input("Enter your Adhar number:\n")

if(len(name)<=1):
    print("enter write name")
elif int(age)<18:
    print("you are not eligible for voting try next year")
elif len(adhar) != 12:
    print('enter right adhar number ')
else:
    print("you are selected for voting")
