
def ch(c):
    if (c>='a' and c<='z') or (c>='A' and c<='Z'):
        print(c,"is an alphabet")
    else:
        print(c,"is not an alphabet")
c=input("Enter a character: ")
ch(c)