def per():
    n=int(input("Enter a number"))
    sum=0
    for i in range(1,n+1):
        temp=i
        if(temp%i==0):
            sum+=i
        if(sum==n):
            print(i)