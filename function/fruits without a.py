fruits = ["apple","banana","grapes","cherry","kiwi","mango"]

age = [12,34,11,45,43,25,57,61,14,13,16,65]

newlist = [x for x in fruits if "a"in x]
newlist1 = [x for x in fruits if "a" not in x]
age1 = [x for x in age if x<18]
age2 = [x for x in age if x>18]
even = [x for x in age if x%2 ==0]
odd = [x for x in age if x%2  !=0]


print("list not eligible for voting",age1)
print("list eligible for voting",age2)
print(odd)

