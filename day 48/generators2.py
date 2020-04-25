def fibo():
    output = []

    num1 = 0
    num2 = 1
    output.append(num1)
    output.append(num2)
    count = 2
    while(True):
        next_num = num1 + num2
        output.append(next_num)

        count = count+1

        if count == 5:
            yield output
            output = []
            count = 0
        num1, num2 = num2 , next_num

m = fibo()
print(next(m))
print(next(m))
print(next(m))
