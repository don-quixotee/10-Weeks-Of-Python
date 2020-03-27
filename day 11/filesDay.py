"""
mode:
    r : read 
    r+
    
    w : write 
    w+ 
    
    a : append
    a+
"""

fp = open("sample_text.txt","r",encoding="utf-8")
content = fp.read()
print(content)
fp.close()