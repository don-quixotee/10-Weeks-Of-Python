from collections import namedtuple

# list / tuple
color = (55,155,255)
print(color)

# dictionary
color = {'red': 55, 'green': 155, 'blue': 255}
print(color)

# namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
print(color)
color = Color(blue=55,green=155,red=255)

print(color)