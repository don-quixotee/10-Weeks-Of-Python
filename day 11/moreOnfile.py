fp1 = open("file1.txt","r")
fp2 = open("file2.txt","r")
fp3 = open("file3.txt","w")

file1_content = fp1.read()
file2_content = fp2.read()

data = "{} \n\n{}".format(file1_content,file2_content)


fp3.write(data)
fp1.close()
fp2.close()
fp3.close()