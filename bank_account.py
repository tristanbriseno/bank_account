from random import *
#imports ra ndom

def new_acc_num():
    return randrange(10000000, 99999999)
    #creates an account number
    
     
    class BankAccount:

    #Provided BankAccount with attributes
    def __init__(self, full_name, routing_num, balance=0):
    
        self.full_name=full_name
        self.account_num=new_acc_num()
        self.routing_num=routing_num
        self.balance=balance



         #this is the deposit function
    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited: ${amount}")



    #this is the withdraw function
    def withdraw(self, amount):
        if amount > self.balance:
            print("You have Insufficient Funds! you will be charged an overdraft fee of: $10")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Your have withdrawn: ${amount}")