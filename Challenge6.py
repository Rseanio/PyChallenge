import urllib.request
import zipfile, re
from collections import Counter

data = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/channel.zip")
filenumber = "90052.txt"
f = zipfile.ZipFile("channel.zip")
commentslist = []
for x in range(0,10000):
    y = f.read(filenumber)
    commentslist.append(f.getinfo(filenumber).comment.decode()) 
    y = y.decode()
    y = y.split()
    end = y[-1]
    if "comments" in end:
        break
    filenumber = end + ".txt"
print("".join(commentslist))