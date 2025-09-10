def un():
    li=[]
    n=int(input("Enter length:"))
    for i in range(n):
        li.append(int(input("Enter number")))
    li2=set(li)
    li1=list(li2)
    print(li1)
un()