x=float (input ("enter x: "))
y=float (input ("enter y: "))




try:
    ans=x/y
except ZeroDivisionError:
    print("Please enter value in denominator other then ZERO")
else:
    print (x,"/", y, "=",ans)


print ("Have a nice day")