def one_dimensional_booleans(bool_list, use_and):
    if not use_and:
        return True in bool_list
    else:
        return not False in bool_list

print(one_dimensional_booleans([True, True, True], True))
print(one_dimensional_booleans([True, False, True], True))
print(one_dimensional_booleans([True, False, True], False))
print(one_dimensional_booleans([False, False, False], False))
