def circle(radius):
    ans=3.14*radius*radius
    print("Area of circle=",ans)

def circleWithReturn(radius):
    ans = 3.14 * radius * radius
    return ans

circle(8)
circle(9)

ans=circleWithReturn(2)
print("area=",ans)
print("area,=",circleWithReturn(10))