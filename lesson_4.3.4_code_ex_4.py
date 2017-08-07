#We've learned a lot in this chapter. Let's try to use a lot
#of it for one final exercise.
#
#Write a function called sort_artists. sort_artists will
#take as input a list of tuples. Each tuple will have two
#items: the first item will be a string holding an artist's
#name, and the second will be an integer representing their
#total album sales (in millions).
#
#Return a tuple of two lists. The first list in the
#resulting tuple should be all the artists sorted
#alphabetically. The second list should be all the revenues
#sorted in descending numerical order.
#
#For example:
# artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
# sort_artists(artists) -> (["Elvis Presley", "Michael Jackson", "The Beatles"], [270.8, 211.5, 183.9])
#
#Notice that artists is a list of tuples (brackets first,
#then parentheses), but sort_artists outputs a tuple of
#lists (parentheses first, then brackets).


#Write your function here!
def sort_artists(artists):
    artist_names = []
    artist_revenues = []
    intermediate_list = []
    intermediate_artist_list = []
    for tuples in artists:
        for i in tuples:
            intermediate_list.append(i)
    for idx, value in enumerate(intermediate_list):
        if idx == 0:
            artist_names.append(value)
        elif idx % 2 == 0:
            artist_names.append(value)
        else:
            artist_revenues.append(value)
    artist_names.sort()
    artist_revenues = sorted(artist_revenues, reverse=True) #, key=float, reverse=True)
    #artist_revenues.sort()
    #print("Sorted artist names list: ", artist_names)
    #print("Sorted Artist revenues list ", artist_revenues)

    my_new_tuple = (artist_names, artist_revenues)
    return my_new_tuple


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#(['Elvis Presley', 'Michael Jackson', 'The Beatles'], [270.8, 211.5, 183.9])
#artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
artists = [('Taylor Swift', 115.1), ('Celine Dion', 124.6), ('U2', 106.1), ('Led Zeppelin', 139.5), ('AC/DC', 112.9), ('Billy Joel', 102.4), ('Michael Jackson', 183.9), ('Phil Collins', 87.7)]
print(sort_artists(artists))
