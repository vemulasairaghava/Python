def st():
    s1=input("Enter string1")
    c1=0
    c2=0
    s2=input("Enter string2")
    for i in s1:   
        c1+=1
    print("Length of s1 is",c1)
    print("concatenation of two strings",s1+s2)
    if(s1==s2):
        print("both are same")
    else:
        print("not same")
st()