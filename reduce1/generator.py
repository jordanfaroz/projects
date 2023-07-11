def simple():
    for i in range(10):
        if (i%2 == 0):
            yield i




for i in simple():
    print(i)

