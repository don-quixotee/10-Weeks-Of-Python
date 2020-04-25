import itertools


def printval(l):
    for value in l:
        if value == 20:
            return value
        yield value


l = [10,100,30,40,50,20]
g = printval(l)

print(next(g))
print(next(g))
print(next(g))
print(next(g))

""" tuple comprehension is also a for of generators"""
t = (i*i for i in l)
print(t)
print(next(t))