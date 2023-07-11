import functools
import operator

lis = [12, 3, 51, 36, 2, 38, 69, 75, 45 ,67 , 32 ,45]
l1=[80,80,80]

print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))
sum = (functools.reduce(lambda a, b: a + b, l1))


print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))


print("The minimum element of the list is : ", end="")
print(functools.reduce(lambda a, b: b if a > b else a, lis))

print("the average of all the elements in the list is", end="")
print(functools.reduce(lambda a, b: sum/3, l1))


