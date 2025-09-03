def vow(c):
    if c in 'aeiouAEIOU':
        print(c,"is a vowel")
    else:
        print(c,"is a consonant")
c=input("Enter a character: ")
vow(c)