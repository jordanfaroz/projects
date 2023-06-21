nos = list(range(1,1000))
nos1 = list(range(1,100))
nos2 = [23,45,67,65,43,12,67,65,67,65]
nos3 = [45,76,43,12,23,45,43,12,45,46]



divis = [x for x in nos if x%7 == 0]
hav = [x for x in nos1 if '3' in str(x)]

common = [x for x in nos2 if x in nos3]









sentence="Testing numbwe of sPcws in thia swntwncw using list comprihension."
space  = sum(c.isspace()  for c in sentence)
print("the number of spaces are",space)