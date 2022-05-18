# let's create a new dictionary called 'meals'
meals = {"breakfast": "toast", "lunch": "salad", "dinner": "enchiladas"}
# compare this with silly one 
sillyDict = {0: "toast", 1: "salad"}
# so let's use meaningful key names for finding corresponding values easily 

# how to access the value in the dictionary? 
print(meals["breakfast"])
# does this key exist in the meals dictionary? 
print("breakfast" in meals)

# add new key-value pair into the dictionary 
meals["second breakfast"] = "more toast"
print(meals)

# change an existing key-value pair with the new pair 
meals["lunch"] = "Yogurt"
print(meals)

# delete key-value pair in the dictionary 
del(meals["lunch"])
print(meals)

# shows only keys in the dictionary 
print(meals.keys())
# shows only values in the dictionary 
print(meals.values())

# nested dictionary: dictionaries in another dictonary: 
countries = {
    "uk": {
        "capital": "London", 
        "population": 10000
    },
    "germany": {
        "capital": "Berlin", 
        "population": 20000
    }
}
print(countries)
print(countries["germany"])
print(countries["germany"]["population"])
