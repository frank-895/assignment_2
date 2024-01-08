# This program takes a file of text and uses AutoTokenizer to find top 30 occuring words and their counts

from transformers import *

def count_occ(lis):
    "Returns dictionary that counts how occurences of each number in argument lis"
    d = {} # dictionary to store numbers and counts
    for number in lis:
        if str(number) in d: # add to counter if item already included
            d[str(number)] += 1
        else: # create new item if not included
            d[str(number)] = 1
    return d

with open('new_file.txt', 'r') as file: # read in file
    long_string = file.read() # file saved as single string

    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased") # set up tokenizer

    # PREPROCESS TEXT
    long_string.lower() # makes text all lowercase
    long_string.strip() # removes unneccessary newlines
    list_words = long_string.split() # converts string to list

    # DECLARE VARIABLES
    list_tokens = [] # tokens added to this list
    length = len(list_words) # number of words
    split = 500000 # the number of pieces the text will processed in

    # PROCESS TEXT
    for i in range(0, split): # split the text into processable chunks for AutoTokenizer
        current_section = list_words[i*(length//split) : i*(length//split) + (length//split)]
        encoded = tokenizer.encode(' '.join(current_section)) # assigns text unique integer number
        for j in encoded:
            list_tokens.append(j) # add tokens to list

    current_section = list_words[(split - 1) * (length//split):length] # process any text cut off in last section
    encoded = tokenizer.encode(' '.join(current_section)) # assigns text unique integer number
    for i in encoded:
      list_tokens.append(i)  # add tokens to list

    # PRESENT TOP 30 WORDS
    all_tokens = count_occ(list_tokens) # all_words is a dictionary with all tokens and counts
    top_words = sorted(all_tokens, key=all_tokens.get, reverse=True)[:50] # take top words
    count = 0 # to count number of words
    i = 0 # index for top_words
    while count < 30:
        new_word = tokenizer.decode(int(top_words[i]))
        if new_word.isalpha() == True: # only display words - not any other variables created by AutoTokenizer
          print(new_word + "  " + str(all_tokens[top_words[i]])) # print word and its occurence count
          count += 1
        i += 1