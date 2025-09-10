def st():
    s1=input("Enter string1")
    for i in range(len(s1)):
        k=s1.count(s1[i])
        if s1[i] not in s1[:i]:
            print(s1[i],k,sep='',end='')
st()