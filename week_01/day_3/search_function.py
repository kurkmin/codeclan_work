chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

def find_chicken_by_name(chicken_list, chicken_name):
    found_chicken = None 
    for chicken in chicken_list:
        if chicken["name"] == chicken_name:
            found_chicken = chicken 

    return found_chicken 



print(find_chicken_by_name(chickens, "Hetty"))

# write a function finding a user by the id 
users = [
  { "user_id": 1, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 2, "first_name": "Katherine", "last_name": "Johnson" },
  { "user_id": 3, "first_name": "Dorothy", "last_name": "Vaughan" },
  { "user_id": 4, "first_name": "Hen", "last_name": "Solo" },
  { "user_id": 5, "first_name": "Mary", "last_name": "Jackson" },
] 

def find_user_by_id(user_list, id): 
    user_found = None 
    for user in user_list:
        if user["user_id"] == id: 
            user_found = user 
    return user_found

print(find_user_by_id(users, 3))

