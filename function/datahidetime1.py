import math

class sphere:
    __radius=0
    __vol=0

    def __init__(self):
        self.__radius=float(input("Enter radius:"))

    def display (self):
        print ("Radius of sphere:=", self. __radius)
        print ("Volume of sphere:=",self. __vol)

    def volume (self):
        self.__vol=4/3*math.pi*self.__radius**3

ob=sphere()
ob.volume()
ob.display()