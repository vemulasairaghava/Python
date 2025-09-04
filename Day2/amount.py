def count():
    n=int(input("Enter amount"))
    c=0
    if n>2000:
        c+=n//2000
        n=n%2000
    if n>500:
        c+=n//500
        n=n%500
    if n>200:
        c+=n//200
        n=n%200
    if n>100:
        c+=n//100
        n=n%100
    if n>50:
        c+=n//50
        n=n%50
    if n>20:
        c+=n//20
        n=n%20
    if n>10:
        c+=n//10
        n=n%10
    if n>5:
        c+=n//5
        n=n%5
    if n>2:
        c+=n//2
        n=n%2
    if n>1:
        c+=n//1
        n=n%1
    print(c)
count()



