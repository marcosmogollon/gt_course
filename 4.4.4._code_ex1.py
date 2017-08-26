#Write a function called "find_coffee" that expects a
#filename as a parameter. The function should open the
#given file and return True if the file contains the word
#"coffee". Otherwise, the function should return False.
#
#Hint: look up the read() method if you want to do this
#more simply than you might do with readline().


#Write your function here!
def find_coffee(file_name):
    input_file = open(file_name, "r")
    holding_var = ""
    check_list = []
    for i in file_name:
        holding_var = input_file.readline().strip()
        check_list.append(holding_var)
    input_file.close()
    #list comprehention
    if any("coffee" in l for l in check_list):
        return True
    else:
        return False


#You can test your function with the provided files named
#"coffeeful.txt" and "coffeeless.txt". With their original
#text, the lines below should print True, then False. You
#may also edit the files by selecting them in the drop
#down in the top left to try your code with different
#input.
print(find_coffee("coffeeful.txt"))
print(find_coffee("coffeeless.txt"))
