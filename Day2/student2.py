n=int(input("Enter number of students"))
for i in range(n):
    s=input("Enter student name")
    no=float(input("Enter roll number"))
    m1=float(input("Enter mark1"))
    m2=float(input("Enter mark2"))
    m3=float(input("Enter mark3"))
    tot=float(m1+m2+m3)
    avg=tot/3
    round(avg,2)
    print("roll.no",no,"avgerage is ",avg)
    if avg>40:
        print("pass")
        if avg>=80:
            print("Distension")
        elif avg>70 and avg<80:
            print("A grade")
        elif avg>=50 and avg<=70:
            print("B grade")
        elif avg<50:
            print("C grade")
    else:
        print("Fail")