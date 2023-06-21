import threading
import time

def print_hello_three_times ():
    for i in range (3):
        time.sleep (0.7)
        print ("Hello")

def print_hi_three_times () :
    for i in range (3):
        time.sleep (0.5)
        print ("Hi")

t1 = threading. Thread (target=print_hello_three_times)
t2 = threading. Thread (target=print_hi_three_times)
t1.start()
t2.start()