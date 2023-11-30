for word in line_seperated:  # goes through each word
    short_punct = "-'’"
    bool_test = False
    for punctuation in short_punct:
        if punctuation in word and not bool_test:
            bool_test = True
            new_split = word.split(punctuation)
            for word_split in new_split:
                new_word = strip(word_split)
                if len(new_word) > 0:
                    new_line.append(new_word)  # now we have the completed line
    if not bool_test:
        new_word = strip(word)
        if len(new_word) > 0:  # some words could be just ascii
            new_line.append(new_word)  # now we have the completed line
if len(new_line) > 0:  # some lines could be empty
    words.append(
        new_line)  # now we have the completed list of words, separated by line, then separated by word