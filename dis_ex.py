mystery_string = "catcatcatcatcat"
numcat=0
for index in range(len(mystery_string)):
    if mystery_string[index] == "c" and mystery_string[index+1] == "a" and mystery_string[index+2] == "t":
        numcat=numcat+1
print (numcat)
