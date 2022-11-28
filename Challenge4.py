import urllib.request

urlbase = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
end= "12345"
for x in range(0,399):
    full = urlbase + end
    with urllib.request.urlopen(full) as f:
        #print(f.read())
        y = f.read()
        y = y.decode()
        y = y.split()
        print(y)
        end = y[-1]
#peak.html
#print(full)