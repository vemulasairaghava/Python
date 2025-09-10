def ma(n):
    li=[]
    
    for i in range(n):
        num=int(input("Enter element : "))
        li.append(num)
    d=int(input("Enter element to be deleted:"))
    del li[d]
    print(li)
n=int(input("Enter length :"))
ma(n)   