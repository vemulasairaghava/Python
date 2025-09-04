def fir():
    n = int(input("Enter a number: "))
    num = n
    last = n % 10
    while n >= 10:
        n = n // 10
    first = n
    print(f"first{first} and last digit is:{last}")
fir()