import requests
import re

# get url
url = input('Enter a URL (include `http://`): ')

# connect to the url
website = requests.get(url)

# read html
html = website.text

# use re.findall to grab all the links( a basic regualar expression)
links = re.findall('"((http|ftp)s?://.*?)"', html)

# output links
n = 0
for link in links:
    n +=1
    print("------------------------------------------------------")
    print(n,":",link[0])
