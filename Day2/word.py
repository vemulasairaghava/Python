def word():
    n=int(input("Enter a number"))
    d={'0':"Zero",'1':"one",'2':"Two",'3':"Three",'4':"Four",'5':"Five",'6':"six",
       '7':"Seven",'8':"Eigth",'9':"nine"}
    for digit in str(n):
        print(d[digit],end=" ")
    print()
word()