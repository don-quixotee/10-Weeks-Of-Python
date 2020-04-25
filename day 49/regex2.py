"""
Metachar:
    [a-z] : char class : 1 occurance of [a-z] a or b or c or d or ......... or z 
    [0-9] : digit class  [0-9] : 1 occurance 
    [A-Za-z0-9]
    + : atleast one occ should be there if more thats fine 
    * : zero or more occ are allowed
    ^ : start of the string 
    $ : end of the string 
    [0-9]{5}
    [a-z]{2,5}
    ? : optional


    """

import re


r = re.compile('ab')
s = "abcdacdcababacdacaba"
l = re.findall(r,s)
print(l)


r = re.compile("[a-z]")
s = "aba"
l = re.findall(r,s)
print(l)



r = re.compile('[0-9]')
s = "ABsjkf232445fvjfks"
l = re.findall(r,s)
print(l)


print()
r = re.compile("[a-z A-Z][0-9]")
s = "abchb435dhsk34And7F8S0KSD-#@$%^^hgfsh943"
l = re.findall(r,s)
print(l)


r = re.compile("^[a-z]+[0-9]+$")
s = "abcd1234rst56789"
l = re.findall(r,s)
print(l)

r = re.compile("^[a-z]{3}[0-9]{4}$")
s = "ac1234"
l = re.findall(r,s)
print(l)



pan_no = "ABCDE1234A"
# 5 upper char 
# 4 digits 
# 1 upper case char 
pattern = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
l = re.findall(pattern,pan_no)
print(l)



pan_no = "ABCDE1234A"
# 5 upper char 
# 4 digits 
# 1 upper case char 
pattern = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
m = re.search(pattern,pan_no)

if m:
    print(m.group())
else:
    print("Invalid PAN number")



s1 = "python34"

r = re.compile("python[0-9]*?")
l = re.findall(r,s1)
print(l)

num = "(+91)7123456789"
num1 = "7123456789"
r = re.compile("^(\(\+91\))?([6-9][0-9]{9})$")
m = re.search(r,num)
print(m)
if m:
    print(m.group(2))
else:
    print("Invalid contact number")


d = "32-13-2020"
r = re.compile("^(?P<day>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})")
m =  re.search(r,d)
if m:
    print(m.group(2))

