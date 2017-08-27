#Write a function called find_max_sales. find_max_sales will
#have one parameter: a list of tuples. Each tuple in the
#list will have two items: a string and an integer. The
#string will represent the name of a movie, and the integer
#will represent that movie's total ticket sales (in millions
#of dollars).
#
#The function should return the movie from the list that
#had the most sales. Return only the movie name, not the
#full tuple.


#Write your function here!
def find_max_sales(movies_list):
    movies = []
    movie_names = []
    movie_sales = []
    most_sales = 0
    most_sales_index = 0
    # extract all movie names and sales to a list
    for movie in movies_list:
        for i in movie:
            movies.append(i)
    # make two lists
    for i in movies:
        if isinstance(i, int):
            movie_sales.append(i)
        else:
            movie_names.append(i)
    # get the highest amount of sales
    most_sales = max(movie_sales)
    # check which is the highest integer and find the index
    for index, i in enumerate(movie_sales):
        if i == most_sales:
            most_sales_index = index
        else:
            pass
    return movie_names[most_sales_index]







"""
- pull out all values into a list
- iterate through and find the larget integer and the index
- minus one from the list index and return that value (movie name)

OR:
- pull out all values into a list
- make two more lists one for movie name and one for movie sales
- find the larget integer in the sales list and get the index value
- return the same index from the name list
"""

"""
Solution 1
----------
"""
"""
sudo code
- iterate through the master list (for loop enumerate)
- iterate through each tuple (nested for loop)
- make two lists one for movies and one for sales numbers
- search the sales list for the largest number and get the index value
- using the sales index value return the same index value from movie name
"""

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Rogue One
movie_list = [("Finding Dory", 486), ("Captain America: Civil War", 408), ("Deadpool", 363), ("Zootopia", 341), ("Rogue One", 529), ("The Secret Life of Pets", 368), ("Batman v Superman", 330), ("Sing", 268), ("Suicide Squad", 325), ("The Jungle Book", 364)]
print(find_max_sales(movie_list))
