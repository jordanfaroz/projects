def is_prime(n):
  for i in range(2,int(n/2)):
    if (n%i) == 0:
      return print("nope not a prime no")
  return print("it is a prime no yay")


ans=is_prime(9)


