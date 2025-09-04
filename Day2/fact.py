def fac():
    n=int(input("Enter number"))
    fact=1
    i=1
    while(n>0):
        fact=fact*i
        i+=1
        n-=1
    print(fact)
    

