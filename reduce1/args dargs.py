'''def multi(*names):
    print(names[1])
multi("jordee","onkar","nikita","aamer","supriya")'''

'''def intro(**data):
    print("data type of argument",type(data))

    for key,value in data.items():
        print("{} is {} .".format(key,value))

intro(firstname="jordan",lastname="faroz",job="no job")'''


def multi(*name,**roles):
    print("name: ",name)
    print("roles: ",roles)

multi("jordan","onkar",role1="student",role2="also student")
