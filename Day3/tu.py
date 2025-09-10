def tu():
    li=[]
    for i in range(5):
        print("Enter details of student",i+1)
        r=int(input("roll.no: "))
        n=input("Enter name: ")
        m=int(input("Marks: "))
        li.append((r,n,m))
    print(li)
tu()
