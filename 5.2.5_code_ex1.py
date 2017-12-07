#Write a function called linear() that takes two parameters
#- a list of strings and a string. Write this function so
#that it returns the first index at which the string is
#found within the list if the string is found, or False if
#it is not found. You do not need to worry about searching
#for the search string inside the individual strings within
#the list: for example, linear(["bobby", "fred"], "bob")
#should return False, but linear(["bob", "fred"], "bob")
#should return 0.
#
#Use a linear search algorithm (not as scary as it sounds).
#Do not use the list method index -- in this exercise,
#you're actually implementing the way the index method
#works!


#Write your code here!
def linear(string_list, search_string):
    counter = 0
    end_of_list = len(string_list)
    for i in range(0, (end_of_list + 1)):
        try:
            if string_list[i] == search_string:
                return i
                counter += 1
            elif counter == end_of_list:
                return False
        except IndexError as e:
            return False



#Feel free to add code below to test your function.
#string_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#search_string = 'c'

string_list = ['1', '2', '3', '4', '5', '6', '7']
search_string = '19'
print(linear(string_list, search_string))
