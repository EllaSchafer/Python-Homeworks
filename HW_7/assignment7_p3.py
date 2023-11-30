words = open("words.txt", "r")  # opens the word file
word_list = words.read()  # reads the words
keys = list(word_list.split('\n'))
dict_of_words = {}

# makes dictionary of dictionary
for word in keys:
    temp_list = []
    for char in word:  # creates a list of characters
        temp_list.append(char)
        temp_list.sort()
    dict_of_words.setdefault(tuple(sorted(temp_list)), []).append(word)  # creates a dictionary with characters as a key
    # appends the word that is focused on to the end of the item list

for key in dict_of_words:
    if len(dict_of_words[key]) > 1:
        print(dict_of_words[key])
