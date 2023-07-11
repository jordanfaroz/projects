'''def display(text):
    return text.upper()

print(display("python decorators"))
z = display
print(z("storing function in variable"))
fun = display
print(fun("belated happy birthday"))'''


'''def display(text):
    return text.upper()
def show(text):
    return text.lower()

def highorder(func):
    final_res=func("i am created by function passed as argument")
    print(final_res)

highorder(display)
highorder(show)'''



'''def outer(x):
    print("in outer")
    def inner(y):
        print("in inner")
        return x+y
    return inner
'''

'''add = outer(56)
print(add(71))'''



'''def square_args(func):
  def inner(a):
    return func(a ** 2)
  return inner

print(square_args(6))'''


def outer_div(func):
    print("salary")
    def inner(x):
        if(x>50000):
            x = x*15/100
            return func(x)
    return inner
@outer_div
def divide(x):
    print("your commision is")
    print(x)

#divide1 = outer_div(divide)
divide(56000)



