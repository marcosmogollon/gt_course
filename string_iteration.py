mystery_string = "cacacat cacacat"
count = 0
for number in range(len(mystery_string)):
    if mystery_string[number] == "c" and mystery_string[number + 1] == "a" and mystery_string[number + 2] == "t":
        count += 1
    else:
        continue
print(count)
