import itertools

my_list = [1,2,3,5,6]

combinations = itertools.combinations(my_list, 2)
for c in combinations:
    print(c, end=" ")

permutations = itertools.permutations(my_list, 2)
for p in permutations:
    print(p, end="")