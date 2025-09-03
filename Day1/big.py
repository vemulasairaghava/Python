def big(a,b,c):
    if a>b:
        if a>c:
            print(a,"is the biggest")
        else:
            print(c,"is the biggest")
    else:
        if b>c:
            print(b,"is the biggest")
        else:
            print(c,"is the biggest")
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
big(a,b,c)