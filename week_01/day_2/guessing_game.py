guess = input("what animal am i thinking of? ").lower()
print("You guessed: "+ guess)

if guess == "chicken": 
    print("Correct!")
elif guess == "dog":
    print("No, but I do like dogs.")
elif guess == "cat": 
        print("Cats are cute.")
else:
    print("Better luck next time.")

