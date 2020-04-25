import itertools

l = [10,30,40,50,60,70]
i = iter(l)
# i.append(10)
print(i)
print(next(i))
print(next(i))





l1 = [10,20,30,40,50]
l2 = ["python", "java", "c"]
l3 =  range(100, 115)

i = itertools.chain(l1,l2,l3)
print(i)
for value in i:
    print(value)



l = [10,20,30,40,50,60]
i = itertools.cycle(l)
count = 0 
for value in i:
    if count <20:
        print(value)

    else:
        break
    count = count +1
    