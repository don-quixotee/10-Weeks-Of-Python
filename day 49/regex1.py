import re

a = "abc@xyz.com"
b = "123@xyz.com"
c = "abc123@xyz.com"
d = "abc@xyz.co.in"
e = "ab@ac@xyz.com"
f = "ab._cd.df.12@xyz.com"
# .[a-z0-9] and _[a-z0-9]

##########################################################################

r = re.compile("^[a-z0-9]+([\._][a-z0-9]+)*@[a-z0-9]+(\.[a-z]{2,3}){1,2}$")
m = re.search(r,f)
if m:
    print(m.group())
else:
    print("Invlid email")



r = re.compile("\.")
s = ".abc"
m = re.search(r,s)
if m:
    print(m.group())
else:
    print("Invalid")


###########################################################################


a = "http://www.xyz-a.com"
r = re.compile("^https?://www\.\w+(-\w+)*(\.[a-z]{2,3}){1,2}$")
m = re.search(r,a)
if m:
    print(m.group())
else:
    print("Invalid URL")
    