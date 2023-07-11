num = int(input("enter a positive no"))
i = 1
sum = 0



while i<num:
    if num%i == 0:
        sum = sum + i
    i = i+1

if sum == num:
    print("it is a perfect no")
else:
    print("nope")
