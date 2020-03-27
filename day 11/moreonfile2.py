fp1 = open("file1.txt","r")
fp2 = open("file2.txt","r")
fp3 = open("file3.txt","w")

fp1_fl = fp1.readline().split(" ") 
fp2_fl = fp2.readline().split(" ")

print(fp1_fl)
print(fp2_fl)

pep_file1 = 0
pep_file2 = 0

for value1,value2 in zip(fp1_fl,fp2_fl):
    if pep_file1 !=0 and pep_file2 !=0:
        break
        
    if value1.isdigit():
        pep_file1 = int(value1)
    
    if value2.isdigit():
        pep_file2 = int(value2)

print(pep_file1,pep_file2)

fp1.seek(0)
fp2.seek(0)

file1_content = fp1.read()
file2_content = fp2.read()

if pep_file1 < pep_file2:
    data = "{} \n\n{}".format(file1_content,file2_content)
else:
    data = "{} \n\n{}".format(file2_content,file1_content)

fp3.write(data)

fp1.close()
fp2.close()
fp3.close()