
words = open("words.txt", "r")  # opens the words file
word_list = words.read()  # reads the words
keys = word_list.split()  # splits up the words
set_keys = set(keys)  # turns the words into a set
set_to_track = set()  # used to track all the used words

x = 1  # initializes x
while x < len(keys):
    # values that reset each loop
    non_rotated_word = keys[x]  # initializes word that its on
    rotated_word = keys[x]  #
    y = 1  # initializes y

    while y < (len(non_rotated_word) - 1):
        rotated_word = rotated_word[y:] + rotated_word[:y]
        if rotated_word in set_to_track:  # if the word has already been used, break the loop
            break
        elif rotated_word == non_rotated_word:  # if the rotated word is itself, continue on
            continue
        elif rotated_word in set_keys:  # if the rotated word is real
            print(non_rotated_word, 'rotation of', rotated_word)  # print the rotation
            set_to_track.add(rotated_word)  # this adds the rotated word to a set, ensuring that it
            # doesn't get called twice
            continue  # allows the program to search for words that may have multiple rotations
        y += 1  # counter for inner while loop
    x += 1  # counter for outer while loop
