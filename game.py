import random
'''
-1 for Rock
1 for Paper 
0 for Sezer
'''
computer = random.choice([-1, 0, 1])
Mystr = input("Enter your choice: ")
MyDict = {"R": -1, "P": 1, "S": 0}
reverseDict = {-1: "Rock", 1: "Paper", 0: "Sezer"}

My = MyDict[Mystr]



print(f"You chose {reverseDict[My]}\nComputer chose {reverseDict[computer]}")

if(computer == My):
    print("Its a draw")

else:
    if(computer == -1 and My == 1): 
        print("You win!")

    elif(computer == -1 and My == 0):
        print("You Lose!")

    elif(computer == 1 and My == -1):
        print("You lose!")

    elif(computer == 1 and My == 0):
        print("You Win!")

    elif(computer == 0 and My == -1):
        print("You Win!")

    elif(computer == 0 and My == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")
