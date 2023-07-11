numbers = [66, 78, 2, 45, 97, 17, 34, 105, 44, 52]

idx = len(numbers) - 1
reverse = []

while (idx >= 0):
  reverse.append(numbers[idx])
  idx = idx - 1

print(reverse)