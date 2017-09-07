#Write a function called course_info that takes as input a
#list of tuples. Each tuple contains two items: the first
#item in each tuple is a student's name as a string, and the
#second item in each tuple is that student's age as an
#integer.
#
#The function should return a dictionary with two keys.
#The key "students" should have as its value a list of all
#the students (in other words, a list made from the first
#value of each tuple), in the original order in which they
#appeared in the list. The key "avg_age" should have as its
#value a float representing the average age of all the
#students in the list (in other words, the average of all
#the second items in the tuples).
#
#For example:
#
#  course_info([("Jackie", 20), ("Marguerite", 21)])
#  -> {"students": ['Jackie', 'Marguerite'], "avg_age": 20.5}
#
#Hint: Concentrate first on building the list of students
#and calculating the average age. Save creating the
#dictionary for last.


#Write your function here!
def course_info(list_of_tuples):
    student_names = []
    student_ages = float(0)
    final_dict = {}
    #iterate through the outer list
    for i in list_of_tuples:
        student_names.append(i[0])
        student_ages += i[1]
    #get the number of students to work out the average
    average_divisor = len(student_names)
    average_age = student_ages / average_divisor
    # create the key/value pairs in the dict
    final_dict["students"] = student_names
    final_dict["avg_age"] = average_age
    return final_dict



"""
- Add all student names to a list
- add all the studnt ages to a float
- divide the float by the number of students
- create a dict with the key(studnet_names-list) and a value of the average_age
"""



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
print(course_info([("Jackie", 20), ("Marguerite", 21)]))
