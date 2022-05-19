# this function does not return anything but print the message 
def greet(): 
    print("hey!")

# invoke the function 
greet()

# on the other hand, this function returns something 
def greet():
    return 'hey'

# 'hey' is stored in the function name called 'greeting' since it is more readable
greeting = greet()
print(greeting)

# parameters AND arguments 

def greet2(name):
    return 'hey! ' + name 
print(greet2("min"))

# refactoring e.g. 

def greet(name, time_of_day):
    return "Good " + time_of_day + ", " + name
#Good afternoon, Min is expected to be returned 
print(greet('Min', 'afternoon'))

# any variable created inside the function is in local scope so it cannot be used outside e.g. 

def greet():
    words = "hey"
    return words 
print(greet())

