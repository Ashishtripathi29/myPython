# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
arr=[]
for i in range(0,9):
    position = input("Where do you want to put the treasure? ")
    # 🚨 Don't change the code above 👆

    #Write your code below this row 👇
    if(position not in arr):
       arr.append(position)
    else:
       print("this value is already entered")
       break
    virtical=int(position[0])
    if(virtical>3):
      print("please enter between 0 to 3")
    horizontal=int(position[1])
    map[virtical-1][horizontal-1]='x'



    #Write your code above this row 👆

    # 🚨 Don't change the code below 👇
    print(f"{row1}\n{row2}\n{row3}")

