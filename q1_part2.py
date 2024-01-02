# This program finds the top 30 most common words of new_file.txt and store into a csv file. 

import csv

def count_occ(s):
    "Returns dictionary that counts how occurences of each word in argument string s"
    s = s.strip()
    words = s.split()
    d = {}
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

with open('new_file.txt', 'r') as file1: # read in file
    long_string = file1.read() # variable contains all text as single string
    all_words = count_occ(long_string)
    top_words = sorted(all_words, key=all_words.get, reverse=True)[:30] # take top 30 words
    
    with open('words_counts.csv', 'w', newline="") as file2:
        for word in top_words:
            file2.write(word + "," + str(all_words[word]))
            file2.write("\n")