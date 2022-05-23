# WRITE YOUR FUNCTIONS HERE
# TAKE A HAVE LOOK IT AGAIN!!!
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash_chg):
    pet_shop["admin"]["total_cash"] += cash_chg


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, num_pet_chg):
    pet_shop["admin"]["pets_sold"] += num_pet_chg


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_list.append(pet)
    return breed_list


# needs to be modified!
# test actual data (arguments) should be located in test code NOT IN src code!!!!
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None


def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


# HAVE A LOOK!
def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, cash_chg):
    customer["cash"] -= cash_chg


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    return False


def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):  # it should be modified

        add_pet_to_customer(customer, pet)

        remove_pet_by_name(pet_shop, pet)
        increase_pets_sold(pet_shop, 1)

        remove_customer_cash(customer, pet["price"])

        add_or_remove_cash(pet_shop, pet["price"])
