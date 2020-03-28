nums = [1,2,3,4,5,6,7,8,9,10]

my_list = []
for n in nums:
  my_list.append(n)
print(my_list)

print([n for n in nums])

#finding the square of the list element
my_list = []
for n in nums:
  my_list.append(n*n)
print(my_list)

# Using map and filter
my_list = map(lambda n: n*n, nums)
print(list(my_list))

# getting the even elements from the list
my_list = []
for n in nums:
  if n%2 == 0:
    my_list.append(n)
print(my_list)

# Using a filter  and map for that
my_list = filter(lambda n: n%2 == 0, nums)
print(list(my_list))

# getting a   pair of letters and numbers from "abcd" and "1234"
my_list = []
for letter in 'abcd':
  for num in range(4):
    my_list.append((letter,num))
print(my_list)
print()
print([(i,j) for i in range(0,4) for j in "abcd"])
print()
print([(i,j) for i,j in zip(range(0,4), "abcd")])

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print zip(names, heros)

# getting charater and name pair
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)



# Generator Expressions
# square of the numbrs using yeild
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)
print(list(my_gen))