"""
Demonstrates casting of data types
Author: Abhishek sigh

"""

""" casting with int """
a = int(10)
b = int('10')
d = int(10.10)
print()

print('casting with int()')
print(a, b, d)


""" casting with float""" 
print()
a = float(30)
b = float('30')
c = float('30.5')
d = float(30.5)

print('casting with float()')
print(a, b, c, d)


""" casting with str """
print()

a = str(15)
b = str(15.10)
c = str("15.10")
d = str(True)
e = str([1, 2, 3])
f = str({'1': 'green', '2': 'blue', '3': 'green'})

print('casting with str()')
print(a, b, c, d, e, f)


""" Returns the boolean value of the specified object"""
print()

print('casting with bool()')
print('bool', bool(False))  # False
print('bool', bool(0))      # False
print('bool', bool(None))   # False
print('bool', bool(True))   # True
print('bool', bool(1))      # True
print('bool', bool('0'))    # True
