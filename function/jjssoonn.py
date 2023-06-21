import json

x= '{"name":"JordaN", "age":22, "city":"Mumbai" }'

y =json.loads(x)


print(y["age"])
print(y)