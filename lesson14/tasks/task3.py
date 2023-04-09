def fibonacci():
    a, b = 0, 1
    for x in range(10):
        yield a
        a, b = b, a+b

fib_list = list(fibonacci())
print(fib_list)
