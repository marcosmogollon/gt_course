#Write a function called "load_file" that accepts one
#parameter: a filename. The function should open the
#file and return the contents.#
#
# - If the contents of the file can be interpreted as
#   an integer, return the contents as an integer.
# - Otherwise, if the contents of the file can be
#   interpreted as a float, return the contents as a
#   float.
# - Otherwise, return the contents of the file as a
#   string.
#
#You may assume that the file has only one line.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - Remember, anything you read from a file is
#   initially interpreted as a string.


#Write your function here!
def load_file(file_name):
    input_file = open(file_name, "r")
    check_var_type = input_file.readline()
    try:
        check_var_type = int(check_var_type)
        return check_var_type
    except ValueError:
        try check_var_type = float(check_var_type)
            return check_var_type
        except ValueError:
            return check_var_type
    input_file.close()


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 123, followed by <class 'int'>.
contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))
