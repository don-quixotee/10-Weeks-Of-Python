
fp = open("sample_text2.txt","w+")
print(fp.tell())
s = "Add this to my file"
fp.write(s)
print(fp.tell())
fp.seek(0,0)
print(fp.tell())
content = fp.read()
print(fp.tell())
print(content)
fp.close()