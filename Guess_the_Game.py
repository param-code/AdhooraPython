#Guess the number GAME
NUMBER = 100
i = 0
while(True):
    print("NUMBER_OF_GUESSES Used =",i)
    print("NUMBER_OF_GUESSES Left =",5-i)
    n = int(input("Enter your Number"))
    i += 1
    if n < NUMBER:
        print("Bda Daaalo")
    elif n > NUMBER:
        print("Chhota Daalo")
    else:
        print("Congratulations! You guessed it right.")
        break