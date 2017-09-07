#Write a function called "reader" that reads in a ".cs1301"
#file described in the previous problem. The function should
#return a list of tuples representing the lines in the file like so:
#
#[(line_1_number, line_1_assignment_name, line_1_grade, line_1_total, line_1_weight),
#(line_2_number, line_2_assignment_name, line_2_grade, line_2_total, line_2_weight)]
#
#All items should be of type int except for the name (string)
#and the weight (float). You can assume the file will be in the
#proper format -- in a real program, you would use your code
#from the previous problem to check for formatting before
#trying to call the function below.
#
#Hint: Although you could use readlines() to read in all
#the lines at once, they would all be strings, not a list.
#You still need to go line-by-line and convert each string
#to a list.


#Write your function here!
def reader(input_file):
    reading_list = []
    file_name = open(input_file, "r")
    for i in file_name:
        reading_list.append(i.strip().split())
    file_name.close()
    try:
        #var for tracking the weight
        weight_count = []
        reading_list_length = len(reading_list)
        for sub_list in reading_list:
            outer_list_count = 0
            count = 0
            for i in sub_list:
                if count == 0:
                    location = count
                    sub_list.remove(i)
                    sub_list.insert(location, int(i))
                    count += 1
                elif count == 1:
                    location = count
                    sub_list.remove(i)
                    sub_list.insert(location, str(i))
                    count += 1
                elif count == 2:
                    location = count
                    sub_list.remove(i)
                    sub_list.insert(location, int(i))
                    count += 1
                elif count == 3:
                    location = count
                    sub_list.remove(i)
                    sub_list.insert(location, int(i))
                    count += 1
                elif count == 4:
                    location = count
                    sub_list.remove(i)
                    sub_list.insert(location, float(i))
                    count += 1
                    # append value to weight tracking list
                    weight_count.append(float(i))
            if outer_list_count < reading_list_length:
                new_tuple = tuple(sub_list)
                location = outer_list_count
                reading_list.remove(sub_list)
                reading_list.insert(location, new_tuple)
    except ValueError:
        pass
    reading_list.reverse()
    return reading_list



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[(1, 'assignment_1', 85, 100, 0.25), (2, 'test_1', 90, 100, 0.25), (3, 'exam_1', 95, 100, 0.5)]

print(reader("sample.cs1301"))
