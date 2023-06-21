def cylinder_volume (height, radius):
    volume = height * 3.14 * radius * radius
    return volume

def cylinder_SA (height, radius):
    SA = (2 * 3.14 * radius * height) + (2 * 3.14 * radius * radius)
    return SA


print(cylinder_volume(1,7))
print(cylinder_SA(1,7))
