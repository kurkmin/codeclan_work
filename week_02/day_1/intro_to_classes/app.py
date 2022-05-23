from modules.bank_account import *

# bank_account = BankAccount() 
# print(bank_account)

# it will print something not meaningful 
# <modules.bank_account.BankAccount object at 0x7fa23010efd0>
# object is stored at memory address: 0x7fa23010efd0 

bank_account = BankAccount("John", 500, "business")  
bank_account2 = BankAccount("Jarrod", 1000, "personal")

bank_account.holder_name = "Mike"


print(bank_account.holder_name) 
print(bank_account2.holder_name)

bank_account.pay_in(50)
# pay_in is method 
# this chanages holder_name from "John" to "Jarrod"
print(bank_account.balance)


bank_account.pay_monthly_fee()
print(bank_account.balance)

bank_account2.pay_monthly_fee()
print(bank_account2.balance)

# FT: TypeError: BankAccount() takes no arguments ? when there is only pass under class Bankaccount 
# ST: we put def __init__(self, input_hodler_name, input_balance, input_type): 
# <modules.bank_account.BankAccount object at 0x7fc6780aefd0> 

# objects are instances of class 

# behaviours = methods 

# built-in behaviours = .method()
