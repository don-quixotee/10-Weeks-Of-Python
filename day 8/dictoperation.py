"""

dict :
        mutable 
        unordered 
        all the keys should be unique 
        all the keys should be immutable int, str,float and tuple 
        
Add :
d[key] = value 
 setdeafult 
    
Update :
    d[key] = new value 
    
Delete:
    popitem 
    del
    clear 
    pop("key")
"""

print()

d = {1:1,2:4,3:9}
d.setdefault(3,20)

print(d)

print()


l1= [1,2,3,4,5]
l2 = [1,4,9,16,25]
t = list(zip(l1,l2))
print(t)

print()

d1 = {1:1,2:4,3:9}
d2 = {3:16,5:25}
d1.update(d2)
print(d1)

print()
