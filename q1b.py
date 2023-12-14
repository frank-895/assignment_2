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

with open('new_file.txt', 'r') as file: # read in file
    long_string = file.read() # variable contains all text as single string
    all_words = count_occ(long_string)
    top_words = sorted(all_words, key=all_words.get, reverse=True)[:30] # take top 30 words
    for i in range(0,30):
        top_words[i] = (top_words[i], all_words[top_words[i]]) # include count in final list

with open('words_counts.txt', 'w') as file:
    for word in top_words: # write top_words to new file
        file.write(word[0] + " " + str(word[1]))
        file.write("\n")