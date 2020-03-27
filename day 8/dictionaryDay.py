import random
"""

Dict :
    - mutable add,update and delete 
    - unordered - indeing and slicing not supported  
    - all keys should be unique
    - all the keys should be immutable : int,str,tuple,float

"""
d = {"name":"abhi"}
print(type(d), d)

d = {"name":"abc","email":"abc@gmail.com","age":50}
d['contact'] = "9123456789"
print(d)




print("_"*50)
print(d.get("id",-1))
print(d.setdefault("id"))
print(d)
print("_"*50)
print()

""" getting input in a list using loop"""
d = {}
for num in range(1,11):
    d[num] = num ** 2
    
print(d)

""" getting input using loop and setdefault """
d = {}
for num in range(1,11):
    d.setdefault(num,random.randrange(1,50))
    
print(d)

print("."*100)
print()

"""  creating a dictionary of tuples  by taking input from user"""


d = {}
for num in range(1,92,10):
    d.setdefault((num,num + 9),(num + random.randrange(1,100)))
print(d)
