class BankAccount: 
    # this is method as it is attachted to BankAccount class 
    # self means current object i am referring to 
    # initialising = init 
    def __init__(self, input_hodler_name, balance, input_type):
        self.holder_name = input_hodler_name # instance variable can live outside __init__ method throught whole class file 
        self.balance = balance 
        self.type = input_type 
        self._rates = {
            "personal": 10, 
            "business": 50, 
            "student": 0
        }
    
    # this is method as it is attachted to BankAccount class  
    def pay_in(self, amount):
        self.balance += amount 

    # it is really 
    def pay_monthly_fee(self):
        self.balance -= self._rates[self.type]