import random
"""

gen_pass()
    8 chars 
    - 1 upper 
    - 1 lower 
    - 1 special char [!@#$&]
    - 5 digits
"""
lower = chr(random.randint(ord('a'),ord('z')))
print(lower)

upper = chr(random.randint(ord('A'),ord('Z')))
print(upper)

chars = ['!','@','#','$','&']
special = random.choice(chars)
print(special)

digits = random.randint(10000,99999)
print(digits)