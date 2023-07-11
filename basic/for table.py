n = int(input("Please Enter any Number: "))

print ("The Multiplication Table of: ", n)
for count in range(1, 11):
   print (n, 'x', count, '=', n * count)