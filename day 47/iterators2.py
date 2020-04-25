import itertools


""" finding permutation and combinations using 
itertools"""

l = [10,20,30]
print(list(itertools.combinations(l, 2)))
print(list(itertools.permutations(l,2)))


l1 = [10,20,30,40,50]
l2 = ["python", "java", "c"]
l3 = range(100,105)
i = itertools.chain(l1,l2,l3)
t = itertools.tee(i,5)
print(t)
for value in t[0]:
    print(value)
for value in t[1]:
    print(value)
# for value in t[2]:
#     print(value)
# for value in t[3]:
#     print(value)

# for v in t :
#     print(t)

# print(dir(t))
# print(type(t[1]))


