import threading
import time

x = int(input("enter number to be squared and cubed "))
sq = x*x
cube = x*x*x

def print_square_three_times ():
    for i in range (3):
        time.sleep (0.7)
        print(sq)

def print_cube_three_times () :
    for i in range (3):
        time.sleep (0.5)
        print (cube)

t1 = threading. Thread (target=print_square_three_times)
t2 = threading. Thread (target=print_cube_three_times)
t1.start()
t2.start()