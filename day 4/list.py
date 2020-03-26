
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

print("_"*15 +"operation on list"+ "_"*15)

l = [1,2,4,56,54,3]
print(l)

print("_"*15 +"looping over list"+ "_"*15)
for i in l:
    print(i*i)
print("_"*15 +"list method"+"_"*15)

print(sorted(l))
print(max(l))
print(sum(l))

print("_"*15 +"adding to a  list "+ "_"*15)
m =[]
for i in  range(12):
    m.append(i)
print("_"*15 +"other list methods and operation"+ "_"*15)
print()
print(m.pop)
print(m)
m.extend([1,2])
print(m)







