def li():
    li=[]
    while True:
        print('''Enter 1. Add Product\n
2. Remove Product\n
3. Search Product\n
4. Display Cart\n
5. Count Products\n
6. Exit\n''')
        ch=int(input("Enter your choice"))
        match ch:
            case 1:
                li.append(input("Enter element to add"))
                print(li[len(li)-1],"is added")
            case 2:
                li.remove(input("Enter product to be deleted"))
                print(li)
            case 3:
                s=input("Enter product to be search")
                if s in li:
                    print(li.index(s),"is index of product",s)
            case 4:
                print("product in cart are",li)
            case 5:
                print("Count Products",len(li))
            case 6:
                exit
li()