n=int(input("Enter number:"))
y =0
while(n>0):
    y=y+1
    n=n//10
    if n%2==0:
        print(n)
print("The number of even digits in the number are:",y)