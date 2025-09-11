class BankAccount:
    __balance=0
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount>self.__balance:
            print("money insufficient")
        else:
            self.__balance-=amount
    def get_balance(self):
        print(f"Balance is {self.__balance}")
b=BankAccount()
b.deposit(100)
b.get_balance()
b.withdraw(500)
b.get_balance()
