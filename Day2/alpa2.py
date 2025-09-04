def alp():
    n=input("Enter alpha")
    curr='a'
    while(curr<=n):
        print(curr,end=" ")
        curr=chr(ord(curr)+1)
    print()
alp()
