def div(a):
    if a%5==0 and a%11==0:
        print(a,"is divisible by 5 and 11")
    else:
        print(a,"is not divisible by 5 and 11")
a=int(input("Enter a number"))
div(a)