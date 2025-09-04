def s():
    n=int(input("Enter number"))
    m=int(input("Enter number"))
    for i in range(n):
        for j in range(m):
            if(i==j or i+j==m+1):
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
s()
    