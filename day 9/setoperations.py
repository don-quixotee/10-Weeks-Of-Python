print()
print("creating set from a list and sorting it")
l1 = [10,245,41,20,45,78,10,20,30,40]
l2 = [100,200,300,10,20,78,20,30]
l3 = l1 + l2
s = set(l3)
print(sorted(s))

print()
print("creating a set form string ")
s = "abcdeaaaccdddeedddsssss"
s1 = set(s)
print(s1)

print()

print("counting the most occured character")
max_count = 0
max_char = ""

for char in s1:
    if s.count(char) > max_count:
        max_char = char
        max_count = s.count(char)
        
print(max_char,max_count)
print()


s = "aaabbcdeeeeeeeeeeeeeeeeeeeeedddaaaaaaassdd"
unique_char = []
max_count = 0
max_char = ""

for char in s:
    if char in unique_char:
        continue
    else:
        print(char)
        current_char_count = s.count(char)
        unique_char.append(char)
        if current_char_count > max_count:
            max_char = char
            max_count = current_char_count
            
print(max_char,max_count)

print()

s = set()
s.add(10)
print(s)

print()

s1 = {100,200}
s2 = {10,20,30,40,50}
s1.update(s2)
print(s1)


print()
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

s1.intersection_update(s2)
print(s1)



print()

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

s1.difference_update(s2)
print(s1)

print()

"""
Delete :

    del
    clear 
    
    pop
    discard 
    remove
"""

s = {10,20,30,40,50,60}
print(s)
r = s.pop()
print(s,r)


print()

s = {10,20,30,40,50,60}
print(s)
s.remove(30)
print(s)