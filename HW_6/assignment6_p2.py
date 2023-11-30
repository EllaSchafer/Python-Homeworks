words = open("words.txt", "r")
word_list = words.read()
keys = word_list.split()
set_keys = set(keys)

# goes through all the words in keys
for w in keys:
    if w == w[::-1]: # if the word is the same front to back, continue
        continue
    elif w[::-1] in set_keys: # if it is in
        print(w, "inverse of", w[::-1])
        keys.remove(w) # gets rid of w so there are no duplicates
        keys.remove(w[::-1]) # gets rid of inverse w for no duplicates













