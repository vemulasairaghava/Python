cno=int(input("Enter consumer number"))
name=input("Enter name")
punit=int(input("Enter present month reading"))
lunit=int(input("Enter last month reading"))
unit=punit-lunit
bill=unit*3.80
print("Consumer number: ",cno,"name: ",name,"Total units: ",unit,"bill: ",bill)
