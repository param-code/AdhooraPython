import random
print("Are you Ready to Play the Snake Water Gun GAME!!\n")
Attempts_Left = 10
while True:
    choices = ["S","W","G"]
    computer = random.choice(choices)
    player = input("Type S for Snake , W for Water , G for Gun\n").upper()
    if player == "S" and computer == "W":
        print("You Won!")
    elif player == "S" and computer == "S":
        print("Draw.")
    elif player == "S" and computer == "G":
        print("You Lose!")
    elif player == "W" and computer == "W":
        print("Draw")
    elif player == "W" and computer == "S":
        print("You Lose!!")
    elif player == "W" and computer == "G":
        print("You Won")
    elif player == "G" and computer == "G":
        print("Draw.")
    elif player == "G" and computer == "W":
        print("You Won!")
    elif player == "G" and computer == "S":
        print("You Lose!")
    else:
        print("Invalid Input!!")
    if Attempts_Left == 0:
        break
    print(Attempts_Left)
    Attempts_Left -= 1