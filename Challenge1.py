#Challenge 1, change the following sentence to match the pattern A == C |E == G | etc
string = "pc/def/map.html"
string1 = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
dict = {"/":"/","a":"c","b":"d","c":"e","d":"f","e":"g","f":"h","g":"i","h":"j","i":"k","j":"l","k":"m","l":"n","m":"o","n":"p","o":"q","p":"r","q":"s","r":"t","s":"u","t":"v","u":"w","v":"x","w":"y","x":"z","y":"a","z":"b","'":"'",".":".","(":"(",")":")"}
newstring = ""
for x in string:
    if x == " ":
        newstring = newstring + " "
    else:
        newstring = newstring + (dict[x])
print(newstring)
#i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
