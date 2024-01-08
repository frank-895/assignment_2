import spacy
import scispacy
from transformers import AutoTokenizer

model1 = spacy.load("en_core_sci_sm")
model2 = spacy.load("en_ner_bc5cdr_md")

word_list_1 = []
word_list_2 = []

with open('new_file.txt', 'r') as file1:
    long_string = file1.read()
    long_string = long_string.splitlines()
    for section in long_string:
      
      temp = model1(section)
      for i in temp.ents:
        if i not in word_list_1:
          word_list_1.append(i)
      temp = model2(section)
      for i in temp.ents:
        if i not in word_list_1:
          word_list_1.append(i)

print(len(word_list_1))
print(word_list_1)
