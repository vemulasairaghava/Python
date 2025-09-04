cno=int(input("Enter consumer number"))
name=input("Enter name")
punit=int(input("Enter present month reading"))
lunit=int(input("Enter last month reading"))
tunit=punit-lunit
if tunit>300:
    bill=(50*3.80)+(50*4.20)+(100*5.1)+((tunit-300))*7.5+(100*6.3)
    print(bill)
elif tunit>200:
    bill=(50*3.80)+(50*4.20)+(100*5.1)+(tunit-200)*6.3
    print(bill)
elif tunit>100:
    bill=(50*3.80)+(50*4.20)+((tunit-100)*5.1)
    print(bill)
elif tunit>50:
    bill=(50*3.80)+((tunit-50)*4.2)
    print(bill)
else:
    bill=tunit*3.8
    print(bill)
