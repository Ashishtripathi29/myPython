print("welcome to pizza hotal\n")
print('which size of pizza would you like:\n')
print('1. small\n2. medium\n3. large\n')
size=input()
pepp=input('would you like to pepperoni enter "y" and "n": ')
cheese=input('would you like to extra cheese enter "y" and "n": ')
charge=0
if(cheese=='y'):
    charge+=1
if(size=='1'):
    charge+=15
    if(pepp=='y'):
        charge+=1
elif size=='2':
    charge+=20
    if(pepp=='y'):
        charge+=2
elif size=='3':
    charge+=25
    if(pepp=='y'):
        charge+=3
else:
    print('please enter right value')
print('you have to pay $'+ str(charge) )