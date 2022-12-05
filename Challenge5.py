#PEAK HELL
import pickle
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/banner.p"

raw = pickle.load(urllib.request.urlopen(url))
for line in raw:
    print("".join([k * v for k, v in line]))
#pickle(url)
#SOMETHING IS IN BORDER.P