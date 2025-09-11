
class Payment():
    def pay(self):
        pass
class CashPayment(Payment):
    
    def pay(self,amount):
        print(f"Paid {amount} in cash")

class CardPayment(Payment):
    
    def pay(self,amount):
        print(f"Paid {amount} using card")
        
class UPIPayment(Payment):
    
    def pay(self,amount):
        print(f"Paid {amount} using upi")
c1=CashPayment()
card=CardPayment()
u=UPIPayment()
l=[c1,card,u]
for i in l:
    i.pay(100)
