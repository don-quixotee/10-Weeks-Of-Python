"""
Delete:
    popitem
    pop
    del
    clear
"""
#popitem:- deletes an item from last index

print()

d = {"maths":55,"phy":35,"chem":25,"eng":80}

print(d)
print()
r = d.popitem()
print(d,r)



print()

#pop


d = {"maths":55,"phy":35,"chem":25,"eng":80}
r = d.pop("phy")
print(d,r)