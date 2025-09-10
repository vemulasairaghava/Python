def ma(n):
    li=[]
    ce=0
    co=0
    for i in range(n):
        num=int(input("Enter element"))
        li.append(num)
        if(li[i]%2==0):
            ce+=1
        else:
            co+=1
    print("Even count",ce,"odd count",co)
n=int(input("Enter length"))
ma(n)