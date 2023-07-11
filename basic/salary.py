input("enter your name")
x = int(input("enter you salary"))

commision = x*10/100
HRA = x*15/100
PF = x*7/100
net = x + commision + HRA - PF

print("your comission is",commision)
print("your HRA is",HRA)
print("your pf is",PF)
print("your net salary is",net)
