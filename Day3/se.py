def se():
    s=set()
    n=int(input("Enter length"))
    for i in range(n):
        ele=input("Enter ele")
        s=s|{ele}
    print(s)
se()