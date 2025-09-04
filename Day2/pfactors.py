def prime(n):
    c=0
    for i in range(2,n+1):
        if(n%i==0):
            c+=1
        if(c==1):
            return i
def factors():
    n=int(input("Enter a number"))
    for i in range(1,n+1):
        if(prime(i)):
            if(n%i==0):
                print(i)

factors()
