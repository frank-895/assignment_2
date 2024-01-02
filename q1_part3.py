from transformers import *


with open('new_file.txt', 'r') as file1:
    long_string = file1.read()
    tokenizer = AutoTokenizer.from_pretrained('google/flan-t5-base')
    encoding = tokenizer(long_string)
    print(encoding)