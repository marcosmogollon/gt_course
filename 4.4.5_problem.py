#Write a function called get_grade that will read a
#given .cs1301 file and return the student's grade.
#To do this, we would recommend you first pass the
#filename to your previously-written reader() function,
#then use the list that it returns to do your
#calculations. You may assume the file is well-formed.
#
#A student's grade should be 100 times the sum of each
#individual assignment's grade divided by its total,
#multiplied by its weight. So, if the .cs1301 just had
#these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
#Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


#Write your function here!
def get_grade(file_name):
    returned_list = reader(file_name)
    running_score = float(0)
    interim_score = float(0)
    final_score = float(0)
    # iterate through all the sublists
    for i in returned_list:
        interim_score = ((i[2]/i[3]) * i[4])
        running_score += interim_score
    final_score = running_score * 100
    return final_score

# reader function
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
#print: 91.55
print(get_grade("sample.cs1301"))
