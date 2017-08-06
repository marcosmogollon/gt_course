#Last exercise, you wrote a function called
#one_dimensional_booleans that performed some reasoning
#over a one-dimensional list of boolean values. Now,
#let's extend that.
#
#Imagine you have a two-dimensional list of booleans,
#like this one:
#[[True, True, True], [True, False, True], [False, False, False]]
#
#Notice the two sets of brackets: this is a list of lists.
#We'll call the big list the superlist and each smaller
#list a sublist.
#
#Write a function called two_dimensional_booleans that
#does the same thing as one_dimensonal_booleans. It should
#look at each sublist in the superlist, test it for the
#given operator, and then return a list of the results.
#
#For example, if the list above was called a_superlist,
#then we'd see these results:
#
# two_dimensional_booleans(a_superlist, True) -> [True, False, False]
# two_dimensional_booleans(a_superlist, False) -> [True, True, False]
#
#When use_and is True, then only the first sublist gets
#a value of True. When use_and is False, then the first
#and second sublists get values of True in the final
#list.


#Write your function here!
def two_dimensional_booleans(bool_superlist, use_and):
    length_of_super_bool_list = len(bool_superlist)
    if use_and is False:
        for bool_sub_list in bool_superlist:
            result = []
            #print("\nThis is one loop pass with the use_and value of: False\n")
            false_count = 0
            for num in bool_sub_list:
                if num is False:
                    false_count += 1
                else:
                    pass
                if false_count == len(bool_sub_list):
                    result.append(False)
                    #print("False")
                else:
                    result.append(True)
                    #print("True")
        #slice the result list down to contain ONLY the number of elements as the length of the super book list eg: supoer bool list is 3 elements long slice results to 3 emements
        result = result[0:length_of_super_bool_list]
        return result
    elif use_and is True:
        result = []
        for bool_sub_list in bool_superlist:
            #print("\nThis is one loop pass with the use_and value of: True\n")
            true_count = 0
            for num in bool_sub_list:
                if num is True:
                    true_count += 1
                else:
                    pass
            if true_count == len(bool_sub_list):
                result.append(True)
                #print("True")
            else:
                result.append(False)
                #print("False")
        result = result[0:length_of_super_bool_list]
        return result

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[True, False, False]
#[True, True, False]
#bool_superlist = [[True, True, True], [True, False, True], [False, False, False]]
#bool_superlist = [[True, True], [True, False, True, False], [True, False, False, False, True, True]]
bool_superlist = [[True, True], [True, True], [False, True, False], [True, False, False]]
print(two_dimensional_booleans(bool_superlist, True))
print(two_dimensional_booleans(bool_superlist, False))
