#Write a function called "angry_file_finder" that accepts a
#filename as a parameter. The function should open the file,
#read it, and return True if the file contains "!" on every
#line. Otherwise the function should return False.
#
#Hint: there are lots of ways to do this. We'd suggest using
#either the readline() or readlines() methods. readline()
#returns the next line in the file; readlines() returns a
#list of all the lines in the file.


#Write your function here!
def angry_file_finder(file_name):
    input_file = open(file_name, "r")
    holding_var = ""
    check_list = []
    count_instances = 0
    for i in file_name:
        holding_var = input_file.readline().strip()
        check_list.append(holding_var)
    input_file.close()
    # remove all the empty strings from the list
    check_list[:] = [item for item in check_list if not item == '']
    # check a ! exists in every element of the list
    for word in check_list:
        if "!" in word:
            count_instances += 1
    if count_instances == len(check_list):
        return True
    else:
        return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True
print(angry_file_finder("AngryFileFinderInput.txt"))
