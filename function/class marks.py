class marks:



    def __init__(self, h, e,m,s):
        self.hindi = h
        self.english = e
        self.math = m
        self.science = s

    def display(self):
        print("hindi marks = " ,self.hindi)
        print("english marks = ", self.english)
        print("math marks = " , self.math)
        print("science marks = ", self.science)
        print("total marks = ", self.total)
        print("percent marks = ", self.percent)

    def calculate(self):
        self.total = self.hindi + self.english + self.math + self.science
        self.percent = self.total * 100/160





marks1 = marks(23,34,33,32)
marks1.calculate()
marks1.display()