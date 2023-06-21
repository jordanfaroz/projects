class GfG:
    name = "jordan"
    age = 23



obj = GfG()


print("The name is " + getattr(obj, 'name'))


print("Description is " + getattr(obj,
                                  'description',
                                  'CS Portal'))

'''import time



class GfG:
    name = "jordee"
    age = 23


obj = GfG()


start_getattr = time.time()
print("The name is " + getattr(obj, 'name'))
print("Time to execute getattr " + str(time.time() - start_getattr))


start_obj = time.time()
print("The name is " + obj.name)
print("Time to execute conventional method " + str(time.time() - start_obj))
'''




