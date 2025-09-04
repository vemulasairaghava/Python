def armstrong():
    n = int(input("Enter number: "))
    for i in range(1, n):
        temp = i
        sum_digits = 0
        while temp > 0:
            r = temp % 10
            sum_digits += r ** 3
            temp //= 10
        if sum_digits == i:
            print(i)
armstrong()