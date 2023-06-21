class GfG:
    name = "jordee"
    age = 23
   ''' motto = "yo"'''



obj = GfG()


print("Does name exist ? " + str(hasattr(obj, 'name')))


print("Does motto exist ? " + str(hasattr(obj, 'motto')))