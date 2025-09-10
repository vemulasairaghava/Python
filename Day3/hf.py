def st():
    s1=input("Enter string1")
    m=s1.count(s1[0])
    for i in range(1,len(s1)):
        if(s1.count(s1[i])>m):
            m=s1.count(i)
    print(m)
st()