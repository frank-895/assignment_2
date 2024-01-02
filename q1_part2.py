# This program finds the top 30 most common words of new_file.txt and store into a csv file. 

import csv # to write new csv file

def count_occ(s):
    "Returns dictionary that counts how occurences of each word in argument string s"
    s = s.strip() # remove excess characters
    words = s.split() # split into list of words
    d = {} # dictionary to store words and counts
    for word in words:
        if word in d: # add to counter if item already included
            d[word] += 1
        else: # create new item if not included
            d[word] = 1
    return d

with open('new_file.txt', 'r') as file1: # read in file
    long_string = file1.read() # variable contains all text as single string
    all_words = count_occ(long_string) # all_words dictionary contains all word counts
    top_words = sorted(all_words, key=all_words.get, reverse=True)[:30] # take top 30 words
    
    with open('words_counts.csv', 'w', newline="") as file2: # write top 30 words and counts to .csv file
        for word in top_words:
            file2.write(word + "," + str(all_words[word]))
            file2.write("\n")