class marks:


    def __init__(self,h,e,m,s):
        self.hindi = h
        self.english = e
        self.maths=m
        self.science=s


    def display(self):
        print("hindi marks are",self.hindi)
        print("english marks are", self.english)
        print("maths marks are", self.maths)
        print("science marks are", self.science)
        print("total marks are", self.total)
        print("percent marks are", self.percent)

    def calculate(self):
        self.total = self.hindi + self.science + self.english + self.maths
        self.percent = self.total *100/160




obj = marks(34,35,23,28)
obj.calculate()
obj.display()