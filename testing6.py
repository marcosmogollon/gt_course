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
#
#Hint: This problem can be extremely difficult or
#extremely simple. Try to use your answer our our
#code from the sample answer in the previous problem --
#it can make your work a lot easier! You may even want
#to use multiple functions.


#Write your function here!
def two_dimensional_booleans(bool_superlist, use_and):
    length_of_list = (len(bool_list))
    num_of_trues = 0
    if use_and is False:
        for i in bool_list:
            if i is True:
                num_of_trues += 1
            else:
                pass
        if num_of_trues > 0:
            return True
        else:
            return False
    elif use_and is True:
        for i in bool_list:
            if i is True:
                num_of_trues += 1
            else:
                pass
        if num_of_trues == len(bool_list):
            return True
        else:
            return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[True, False, False]
#[True, True, False]
bool_superlist = [[True, True, True], [True, False, True], [False, False, False]]
print(two_dimensional_booleans(bool_superlist, True))
print(two_dimensional_booleans(bool_superlist, False))
