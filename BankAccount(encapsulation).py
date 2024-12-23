class Bankaccount:
    def __init__(self,number,balance):
        self.__number=number
        self._balance=balance

    def get_number(self):
        return account.__number 
    
    def set_number(self,newnumber):
        if len(newnumber)==8 and newnumber.isdigit():
            self.__number = newnumber 
        else:
            print("invalid account number")

    def get_balance(self):
        return self._balance
    
    def deposit(self,amount):
        if amount>0 :
            self._balance += amount 
            print(f" deposited: {amount} . balance = {self._balance}")
        else:
            print(" invalid deposit amount")

    def withdraw(self,amount):
        if 0<amount< self._balance:
            self._balance -= amount 
            print (f" withdrew: {amount} . balance = {self._balance}")
        else:
            print(" insufficient funds")

account=Bankaccount("12345678",1000)
account.set_number("11111111")
print(f"account number: {account.get_number()}")
account.deposit(3000)
account.withdraw(1000)
print(f" balance = {account.get_balance()}")