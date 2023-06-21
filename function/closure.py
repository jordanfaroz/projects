def outer():
    msg="Hello"
    print("outer=",hex(id(msg)))
    def inner():
        print (msg)
        print("inner=",hex(id ( msg)))
    return inner



x=outer ()
print (x())
print(x.__closure__)
print(outer().__closure__)
