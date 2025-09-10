def st():
    s1=input("Enter string1")
    vc=0
    cc=0
    s1.upper()
    for l in s1:
        if l in ('A','E','I','O','U'):
            vc+=1
        else:
            cc+=1
    print("vowels,consonants in string are",vc,cc)
st()
