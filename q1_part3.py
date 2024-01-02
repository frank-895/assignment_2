from transformers import *

def count_occ(lis):
    "Returns dictionary that counts how occurences of each number in argument list lis"
    d = {} # dictionary to store numbers and counts
    for number in lis:
        if str(number) in d: # add to counter if item already included
            d[str(number)] += 1
        else: # create new item if not included
            d[str(number)] = 1
    return d

with open('new_file.txt', 'r') as file1:
    long_string = file1.read()
    long_string = "this is a practice string string frank a frank frank string since the long one doesn't actually work 123 a a a."
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    encoding = tokenizer(long_string)
    ids = encoding['input_ids']
    all_words = count_occ(ids)
    top_words = sorted(all_words, key=all_words.get, reverse=True)[:30] # take top 30 words
    print(top_words)