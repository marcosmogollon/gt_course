mystery_int = 33
while mystery_int >= 0:
    for i in range(mystery_int, 0, -3):
        if mystery_int == 0 or mystery_int < 0:
            print("0")
            break
        else:
            print(i)
            mystery_int -= 3
