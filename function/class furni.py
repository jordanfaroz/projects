class furniture:

    def __init__(self ,hieght , width , color):
        self.hieght = hieght
        self.width = width
        self.color=color


    def show(self):
        print("hieght\t:\t" , self.hieght)
        print("width\t:\t", self.width)
        print("color\t:\t", self.color)

class chair(furniture):

    def __init__(self,hieght,width,color,legs):
        furniture.__init__(self,hieght,width,color)
        self.legs=legs


    def show(self):
        furniture.show(self)
        super(chair, self).show()
        print("legs=",self.legs)

ob=chair(int(input("enter hieght")),int(input("enter width")),input("enter color"),int(input("enter legs")))
ob.show()



