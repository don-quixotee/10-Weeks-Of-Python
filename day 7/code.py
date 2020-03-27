a = [1,2,4,4,5,5]
print('Address of a is: {}'.format(id(a)))

a[0] = ''
print(a)
print('Address of a is: {}'.format(id(a)))