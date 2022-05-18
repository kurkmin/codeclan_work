# create a list (fruits) that contains following: 
fruits = ["apple", "banana", "grape", "orange"]
# print an element positioned at 4th index in that list 
print(fruits[3])

# number of items in the list? 
length = len(fruits)
print(length)

# add item to the list 
fruits.append("pear")
print(fruits)
# remove the element at the number position 
fruits.pop(1)
print(fruits)

# strings and integers together can be in the same list 
fruits_and_numbers = ["apple", 1, 2, 5, "banana", 134, "pear"]
# print an element positioned at 4th index in the list 
nested_list = [1, 2, 3, 4, [5, 6, 7]]
print(nested_list[4])
print(nested_list[4][2])

# now let's do the task 
# 1. create an empty list called 'task_list' 
task_list = [] # or take_list = list()
# 2. add a few 'str' elements, representing some everyday tasks e.g. 'Make Dinner' 
task_list.append('Make Dinner')
task_list.append('Wash Dishes')
# 3. print out 'task_list
print(task_list)
# 4. remove the last task 
task_list.pop()
# 5. print out 'task_list
print(task_list)
# 6. print out the number of elements in 'task_list'
print(len(task_list))

# extend enables appending several items 
task_list.extend(["Walk dog", "Something else"])
print(task_list)
# replace an existing element with new element 
task_list[0] = "Finished"
print(task_list)


# Now let's move onto dictionaries: 
# the disadvantage of using a list is you have to memorise all index numbers to access an element you are looking for / e.g. 
meals = ["toast", "more toast", "salad"]
# so instead of index, it is better to use dictionary which has key and corresponding value to make life easier 
