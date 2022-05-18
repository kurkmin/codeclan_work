# Let's begin with the Exercise A: 

stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
print(stops)
#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St")
print(stops)
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(3, "Polmont") # insert method adds data to the list BEFORE the element at the index number you type 
print(stops)
#4. Print out the index position of "Linlithgow"
print(stops[3])
#5. Remove "Livingston" from the list using its name
stops.remove("Livingston") # remove method removes the mathcing element from the list 
print(stops)
#6. Delete "Cumbernauld" from the list by index
stops.pop(2)
print(stops)
#7. Print the number of stops there are in the list
print(len(stops))
#8. Sort the list alphabetically
stops.sort() # sort method sorts a list alphabetetically 
print(stops)
#9. Reverse the positions of the stops in the list
stops.reverse()
print(stops)
#10 Print out all the stops using a for loop
for stop in stops: 
    print(stop)


# Let's move onto the Exercise B 

users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])
# 2. Get Erik's hometown
print(users["Erik"]["home_town"])
# 3. Get the list of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"])
# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])
# 5. Get the smallest of Erik's lottery numbers
smallest = min(users["Erik"]["lottery_numbers"]) # min function finds the smallest number in the lit 
print(smallest)
# 6. Return an list of Avril's lottery numbers that are even
def only_even(my_list):
    even_list = []
    for element in my_list: 
        if element % 2 != 1: 
            even_list.append(element)
    return even_list
print(only_even(users["Avril"]["lottery_numbers"]))
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])
# 8. Change Erik's hometown to Edinburgh
users["Erik"]["hometown"] = "Edinburgh"
print(users["Erik"]["hometown"])
# 9. Add a pet dog to Erik called "fluffy"
new_dict = {"name": "fluffy", "species": "dog"}
users["Erik"]["pets"].append(new_dict)
print(users["Erik"]["pets"])
# 10. Add another person to the users dictionary
my_dict = {
    "twitter": "kurkmin", 
    "lottery number": [1, 2, 3, 4, 5 , 6],
    "home_town": "Seoul",
    "pets": [
    {
        "name": "lucky",
        "species": "dog"
    }
    ]
    }
users["Sumin"] = my_dict
print(users["Sumin"])


# Let's move onto the Exercise C

united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1]["capital"] = "Cardiff"
print(united_kingdom[1]["capital"])
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
new_dict = {"name": "Northern Ireland", "population": 1811000, "capital": "Belfast"}
united_kingdom.append(new_dict)
print(united_kingdom)
# 3. Use a loop to print the names of all the countries in the UK.
for country in united_kingdom:
    print(country["name"])
# 4. Use a loop to find the total population of the UK. 
total = 0 
for country in united_kingdom:
    total = total + country["population"]
print(total)


# Let's move onto the Exercise D 

#For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_list = []
for num in numbers: 
    if num%2 != 1:
        even_list.append(num)
print(even_list)

# 2. Print the difference between the largest and smallest value:
smallest = min(numbers)
largest = max(numbers)
diff = largest - smallest 
print(diff)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
#for number in numbers:
#    if number == numbers[number+1]:
#        print("true")

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total = 0
for number in numbers: 
    if number != 13: 
        total += number 
print(total)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 