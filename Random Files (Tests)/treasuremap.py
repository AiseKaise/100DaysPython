'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************

'''

from secrets import choice


print("Welcome to the treasure island!!!") 
print("Your mission is to find the treasure")

# case1 = print(input("You have a big mountain infront of you, choose 'L' for left and 'R' for right"))
# if case1 == "L":
#     case2 = print(input("You have a river ahead you type 'S' to swim or 'W' to wait"))
#     if case2 == "W":
#         case3 = print(input("You have 3 options to choose from type 'R' for Red, 'Y' for Yellow, 'B' for Blue"))
#         if case3 == "Y":
#             print("You Won!!!")
#         else:
#             print("you died")
#     else:
#         print("you died")
# else:
#     print("You fell into a hole, Game Over!")

# case1 = print(input("You have a big mountain infront of you, choose 'L' for left and 'R' for right"))
# case2 = print(input("You have a river ahead you type 'S' to swim or 'W' to wait"))
# case3 = print(input("You have 3 options to choose from type 'R' for Red, 'Y' for Yellow, 'B' for Blue"))

# if case1 == "L":
#     print(case2)
# else:
#     print("game over")

# if case2 == "W":
#     print(case3)
# else:
#     print("game over")

# if case3 == "Y":
#     print("you won!")
# else: 
#     print("game over")


choice1 = input("You are at the crossway, where do you wanna go? Type 'left' or 'right'.\n").lower()

if choice1 == "left":
    choice2 = input("You have reached to the riverside, type 'swim' to Swim across or type 'wait' to wait for a boat.\n").lower()
    if choice2 == "wait":
        choice3 = input("You have got 3 mastery boxes, type 'red' to get red one, type 'yellow' to get yellow one, type 'blue' to get blue one\n").lower()
        if choice3 == "yellow":
            print("You got the Tresure Box YYEEYYYEYEYE PARTYYYY!!!!!!!!")
        elif choice3 == "blue":
            print("wrong box game over")
        elif choice3 == "red":
            print("hehe loser")
        else:
            print("Your choose something that doesnt exits, Game over!!!")
    else:
        print("You got attached by sharks and you died, Game Over!")
else: 
    print("You fell into a hole, Game Over!")

