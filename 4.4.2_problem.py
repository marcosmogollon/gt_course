#This is a long one -- our answer is 20 lines of code, but
#yours will probably be longer. That's because it's one of the
#more authentic problems we've done so far. This is a real
#problem you'll start to face if you want to start creating
#useful programs.
#
#One of the reasons that filetypes work is that everyone
#agrees how they are structured. A ".png" file, for example,
#always contains "PNG" in the first four characters to
#assure the program that the file is actually a png. If these
#standards were not set, it would be hard to write programs
#that know how to open and read the file.
#
#Let’s define a new filetype called ".cs1301".
#In this file, every line should be structured like so:
#
#number assignment_name grade total weight
#
#In this file, each component will meet the following
#description:
#
# - number: an integer-like value of the assignment number
#
# - assignment_name: a string value of the assignment name
#
# - grade: an integer-like value of a student’s grade
#
# - total: an integer-like value of the total possible
#   number of points
#
# - weight: a float-like value ranging from 0 to 1
#   representing the percent of the student’s grade this
#   assignment is worth. All the weights should add up to 1.
#
#Each component should be separated with exactly one space.
#A good sample file is available to view as
#"sample.cs1301".
#
#Write a function called format_checker that accepts a
#filename and returns True if the file contents accurately
#conform to the described format. Otherwise the function
#should return False. In other words, it should return True
#if:
#
# - Each line has five elements separated by spaces, AND
# - The first, third, and fourth elements are integers, AND
# - The fifth element is a decimal number, AND
# - All the fifth elements add to 1.
#
#You can make changes to test.cs1301 to test your function,
#or test it with sample.cs1301. Right now, running it on
#sample.cs1301 should return True, and on test.cs1301
#should return False.
#
#Hint 1: .split() will likely help separate each line into
#its components.
#Hint 2: .split() returns a list. So, if you were to do
#something like say split_line = line.split(), then
#split_line[0] would give the first item, split_line[1] would
#give the second item, etc.
#Hint 3: If you're having trouble, try breaking it down by
#parts. First check the file to see if it has the right
#number of items per line, then whether the items are of
#the correct type, then whether the fifth elements add to
#1. Remember, you know how to do each individual check
#(checking types, adding numbers, finding list lengths) --
#the hard part is knitting this all together into one bigger
#solution.


#Write your function here!
def format_checker(input_file):
    reading_list = []
    holding_var = ""
    checking_type = []
    file_name = open(input_file, "r")
    for i in file_name:
        for row in i:
            try:
                int(row)
                reading_list.append(int(row))
            except ValueError:
                try:
                    float(row)
                    reading_list.append(float(row))
                except ValueError:
                    reading_list.append(row.strip().split())
        #if isinstance(i, float):
    #        reading_list.append(float(i))
#        elif isinstance(i, int):
#            reading_list.append(int(i))
#        else:
#            reading_list.append(i.strip().split())
    file_name.close()
    # iterate through each sublist
    #for line in reading_list:
        # check if there are 5 elements in each sublist else throw False
        #if not len(line) == 5:
        #    return False
        #elif not isinstance(line[4], float):
        # check if the 5th element of each sublist is a float AND check that they all add up to 1
            #return False
    print(reading_list)

    # check if the 1st, 3rd and 5th element are integers


    # else return true







"""
new filetype called .cs1301

file structure:
number assignment_name grade total weight

number = int
assignment_name = string
grade/total = int
weight = float (should all add up to 1)

"""












#Test your function below. With the original values of these
#files, these should print True, then False:
print(format_checker("sample_1.cs1301"))
print(format_checker("sample_2.cs1301"))
