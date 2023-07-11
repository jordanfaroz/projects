x = int(input("enter number of seconds"))

seconds = x % 60
min = x % seconds
hrs = x % min

print("time is",hrs,"hrs",min,"minutes and",seconds,"seconds")

