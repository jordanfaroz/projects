no=int (input ("Enter number:"))
eve=0
odd=0
while no>0:
    dig=no%10
    if dig%2==0:
        eve+=1
    else:
        odd+=1
    no=no//10


print("odd=", odd)
print("eve=",eve)
print ("Have a nice Day!!")