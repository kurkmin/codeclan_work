def return_10():
    return 10 

def add(num1, num2):
    return num1 + num2 

def subtract(num1, num2):
    return num1 - num2 

def multiply(num1, num2): 
    return num1 * num2 

def divide(num1, num2):
    return num1 / num2 

def length_of_string(user_string):
    return len(user_string)

def join_string(string_1, string_2):
    return string_1 + string_2 

def add_string_as_number(str_num1, str_num2):
    return int(str_num1) + int(str_num2)

def number_to_full_month_name(num_month):
    month_dict = {
        1: "January", 
        2: "February", 
        3: "March", 
        4: "April", 
        5: "May", 
        6: "Jun", 
        7: "July", 
        8: "August", 
        9: "September", 
        10: "October", 
        11: "November", 
        12: "December"
        }
    return month_dict[num_month]

def number_to_short_month_name(num_month):
    month_dict = {
        1: "January", 
        2: "February", 
        3: "March", 
        4: "April", 
        5: "May", 
        6: "Jun", 
        7: "July", 
        8: "August", 
        9: "September", 
        10: "October", 
        11: "November", 
        12: "December"
        }
    return month_dict[num_month][:3]

def volume_of_cube(user_num):
    return user_num * user_num * user_num 

def reverse_string(user_str):
    return user_str[::-1]

def fahrenheit_to_celsius(f_temp): 
    return float((f_temp-32) * 5 / 9)

