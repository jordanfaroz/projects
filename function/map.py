def myfunc (a):
    if a%2==0:
        return True
    else:
        return False

x=filter(myfunc,[2,3,5,4,6,7])
print(list(x))