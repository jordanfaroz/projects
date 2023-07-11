'''binary = input("Enter a binary number: ")
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print("The decimal equivalent of", binary, "is", decimal)
'''

decimal = int(input("Enter a decimal number: "))
binary = ''

# performing division by 2 until quotient becomes 0
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2

print("The binary equivalent of", decimal, "is", binary)