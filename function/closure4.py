'''lst = []


n = int(input("Enter number of elements : "))


for i in range(0, 6):
    ele = int(input())
    try:
        lst.append(ele)
    except:
        print("list out of range")'''

list=[]


for i in range (1,6):
    list.append(int (input("Enter the element:")))

try:
    no=int (input("Enter the number you want to enter:"))
    print(list[no])
except:
    print("Please enter the index up to:",len(list))

print(list)



