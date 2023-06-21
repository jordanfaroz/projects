def myfunc (a):
    if a>=18:
        return True
    else:
        return False

x=filter(myfunc,[13,54,32,15,45,19,27,12,11,32])
print(list(x))