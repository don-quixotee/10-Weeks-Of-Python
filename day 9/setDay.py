"""
sets:
    - {}
    - all the elemnt should be unique
    - all the elemts should be immutable 
    - as dict {10:None,20:None,30:None}
    - mutable => add update and delete 
    - unordered => no indexing and slicing

"""

print()
print("checking the type of set")

d = set()
print(type(d))

print()
print("changing a list to set")

l = [1,1,2,2,3,4,5,8]
s = set(l)
print(s)


print()

"""
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

s1 union s2 = {10,20,30,40,50,60,70,80}

s1 intersection s2 : {40,50}
    
s1 difference s2 : {10,20,30}
s2 difference s1 ={60,70,80}

s1 symm diff s2 : {10,20,30,60,70,80}
    
s3 = {10,20}
s3 is subset of s1
s1 is superset of s3
"""

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s3 = s1.union(s2)
print(s3)

print()

s4 =s1.intersection(s2)
print(s4)

s5 = s2.difference(s1)
print(s5)

s6 = s1.symmetric_difference(s2)
print(s6)
