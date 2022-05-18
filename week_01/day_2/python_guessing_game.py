my_guess = input("When was Python developed? ")

if not my_guess.isnumeric():
    print("That isn't a number")
elif my_guess == 1991: 
    print("correct!")
else:
    print("Better luck next time.")