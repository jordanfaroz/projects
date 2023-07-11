'''def multiple_yield():
    str1="first string"
    yield str1

    str2 = "second string"
    yield str2

    str3 = "third string"
    yield str3

obj = multiple_yield()
print(next(obj))
print(next(obj))
print(next(obj))'''

'''list = [1,2,3,4,5,6]

sq = [x**3 for x in list]

gn = (x**3 for x in list)

print("list = ",sq)
print("generator = ", gn.__next__() )
print("generator = ", gn.__next__() )
print("generator = ", gn.__next__() )'''



course = ["science", "maths", "english", "hindi", "marathi"]

len1 = (len(x) for x in course)
print("generator = ", len1.__next__() )
print("generator = ", len1.__next__() )




