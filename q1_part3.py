# This program takes a file of text and uses AutoTokenizer to find top 30 occuring words and their counts

from transformers import * # for Auto Tokenizer
import math # for ceiling function

def remove_nonwords(s):
    "Removes nonwords from list s"
    new_list = []
    for word in s:
        if word.isalpha() == True:
            new_list.append(word)
    return new_list

def count_occ(lis):
    "Returns dictionary that counts how occurences of each number in argument lis"
    d = {} # dictionary to store numbers and counts
    for number in lis:
        if str(number) in d: # add to counter if item already included
            d[str(number)] += 1
        else: # create new item if not included
            d[str(number)] = 1
    return d

def auto_tokenise(section, tokens):
    "This function encodes the text in section and adds the tokens to the list called tokens"
    encoded = tokenizer.encode(' '.join(section)) # assigns text unique integer number
    for j in encoded:
        if j != 101 or j != 102:
            tokens.append(j) # add tokens to list

with open('new_file.txt', 'r') as file: # read in file
    long_string = file.read() # file saved as single string

    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased") # set up tokenizer

    # PREPROCESS TEXT
    long_string.lower() # makes text all lowercase
    long_string.strip() # removes unneccessary newlines
    list_words = long_string.split() # converts string to list
    list_words = remove_nonwords(list_words)

    # DECLARE VARIABLES
    list_tokens = [] # tokens added to this list
    length = len(list_words) # number of words
    split = 100000 # the number of pieces the text will processed in
    size_chunk = math.ceil(length / split) # length of each chunk of text rounded up

    # PROCESS TEXT
    for i in range(0, split): # split the text into processable chunks for AutoTokenizer
        if i * size_chunk + size_chunk < length:
            current_section = list_words[i * size_chunk : i * size_chunk + size_chunk]
        else:
            current_section = list_words[i * size_chunk : length]
        auto_tokenise(current_section, list_tokens)

    # PRESENT TOP 30 WORDS
    all_tokens = count_occ(list_tokens) # all_words is a dictionary with all tokens and counts
    top_tokens = sorted(all_tokens, key=all_tokens.get, reverse=True)[:30] # take top words
    
    print("TOP 30 WORDS AND COUNTS")
    for token in top_tokens:
        new_word = tokenizer.decode(int(token))
        print(new_word + "  " + str(all_tokens[token])) # print word and its occurence count