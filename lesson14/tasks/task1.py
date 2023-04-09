def coutdown():
    for num in range(10, -1, -1):
        yield num


gen = coutdown()
for num in gen:
    print(num)

while True:
    print(next(gen))
