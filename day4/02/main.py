
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
arr=[]
pl1=False
pl2=False
for i in range(0,9):
    if(i%2==0):
       position = input("enter the position for first player ")
    else:
       position = input("enter the position for second player ")
       
   
    if(position not in arr):
       arr.append(position)
    else:
       print("this value is already entered")
       break
    virtical=int(position[0])
    horizontal=int(position[1])
    if((virtical>3 or virtical<1 ) or (horizontal>3 or horizontal<1)):
       print("please enter position as for firt in virtical and horizontal 11")
       break

    if(i%2==0):
       map[horizontal-1][virtical-1]='0'
    else:
       map[horizontal-1][virtical-1]='x'
    
    print(f"{row1}\n{row2}\n{row3}")
    if((row1[0]=='0' and row1[1]=='0' and row1[2]=='0') or (row2[0]=='0' and row2[1]=='0' and row2[2]=='0') or  (row3[0]=='0' and row3[1]=='0' and row3[2]=='0') or  (row1[0]=='0' and row2[0]=='0' and row3[0]=='0') or (row1[1]=='0' and row2[1]=='0' and row3[1]=='0') or (row1[2]=='0' and row2[2]=='0' and row3[2]=='0') or (row1[0]=='0' and row2[1]=='0' and row3[2]=='0') or (row1[2]=='0' and row2[1]=='0' and row3[0]=='0')    ):
       print(" first player won the math")
       pl1=True
       break
    elif((row1[0]=='x' and row1[1]=='x' and row1[2]=='x') or (row2[0]=='x' and row2[1]=='x' and row2[2]=='x') or  (row3[0]=='x' and row3[1]=='x' and row3[2]=='x') or  (row1[0]=='x' and row2[0]=='x' and row3[0]=='x') or (row1[1]=='x' and row2[1]=='x' and row3[1]=='x') or (row1[2]=='x' and row2[2]=='x' and row3[2]=='x') or (row1[0]=='x' and row2[1]=='x' and row3[2]=='x') or (row1[2]=='x' and row2[1]=='x' and row3[0]=='x')    ):
       print(" second player won the math")
       pl2=True
       break
if(pl1):
   print("wow first player won the match")
elif(pl2):
   print("second player won the match")
else:
   print("draw match")