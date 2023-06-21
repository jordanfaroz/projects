file1 = open('emp class.py', 'w')
file1.close()

# Using readlines()
file1 = open('emp class.py', 'r')
Lines = file1.readlines(1)

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))