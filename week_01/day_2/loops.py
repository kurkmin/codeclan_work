numbers = [1, 2, 3, 4, 5]
numbers[0] = numbers[0] * 100 
print(numbers)
numbers[1] = numbers[1] * 100 
# it is too repetitive 
# instaed of typing maually, let's use loops (while and for)

# while loop is useful when you want to repeat something until a certain condtion is satisfied 

counter = 0 
my_number = 5 
while counter < my_number:
    print("counter is " + str(counter))
    counter += 1 # counter = counter + 1 


my_number = 5 
value = int(input("What number between 1 and 9 am I thinking of? "))

#while value != my_number:
#    if value > my_number:
#        print("too high")
#    else:
#        print("too low")
#    value =  int(input("Nope! Try again... "))
#print("yes")

hello = 1
# concatenation vs interpolation 
print("You typed: " + str(hello)) 
print(f"You typed: {str(hello)}")

#while (True):
#    line = input("type something: ")
#    if (line.lower() == 'q'):
#        break
#    print(f"you typed: {line}")

# whereas for loop is useful when each element is in the list or in sequqnece 

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number * 3)


total = 0

for number in numbers:
    total = total + number

print(total)


chickens  = ["Margaret", "Hetty", "Henrietta", "Audrey", "Mabel"]

for chicken in chickens:
    print(chicken)

chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Audrey", "age": 2, "eggs": 0},
  {"name": "Mabel", "age": 5, "eggs": 1},
]

for chicken in chickens:
    print(f'{chicken["name"]} is {chicken["age"]}') 

total_eggs = 0

for chicken in chickens:
    if chicken["eggs"] > 0:
        print("wooo eggs!")     
    total_eggs += chicken["eggs"]
# now eggs are collected so it should be zero for each chicken 
    chicken["eggs"] = 0

print(f"{total_eggs} eggs collected")
print(chickens) 


