class customer:
    def __init__(self,name,salary,age,gender):
        self.name = name
        self.salary= salary
        self.age = age
        self.gender=gender


cust1 = customer("jelly",1200000,25,"female")


print(cust1.name)