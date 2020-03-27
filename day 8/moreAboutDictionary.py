
d = {}
for num in range(1,92,10):
    d.setdefault((num,num + 9),0)
print(d)


nums = [10,15,20,25,45,10,12,56,74,85]

for num in nums:
    for x in d:
        if num > x[0] and num <= x[1]:
            d[x] += 1
            break
        
print(d)

print("\n")

""" different operation dictionary"""

d = {1:1,2:4,3:9,4:16}
print(d.keys())
print(d.items())
print(d.values())


print("\n")

""" program to find failed subject"""

d = {"maths":55,"phy":35,"chem":25,"eng":80}
pass_marks = 40
for key,value in d.items():
    if value < pass_marks:
        print(key)




