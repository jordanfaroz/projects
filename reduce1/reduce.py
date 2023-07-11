import functools


def sum(a, b):
    print(f"a={a}, b={b},{a} + {b} = {a + b}")
    return a + b
scores = [1, 2, 3, 4, 5, 6, 7]
total = functools.reduce(sum,scores)
print(total)

