def st():
    s1=input("Enter string")
    ac=0
    dc=0
    sc=0
    for i in s1:
        if i.isalpha():
            ac+=1
        elif i.isdigit():
            dc+=1
        else:
            sc+=1
    print("np.of alphabets in string are",ac,"no.of digits in string are",dc,"no.ofspeical in string are",sc)
st()