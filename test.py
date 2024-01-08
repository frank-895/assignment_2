# import AutoTokenizer to create unique tokens
from transformers import AutoTokenizer

# import Counter to count the repeated unique tokens
from collections import Counter


def count():
    """
        Select the model name from ** Autotokenizer ** that you want to use. 

        'bert-base-uncased' 

        Model description
        BERT is a transformers model pretrained on a large corpus of English data in a self-supervised fashion. 
        This means it was pretrained on the raw texts only, with no humans labeling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts. 
        More precisely, it was pretrained with two objectives:

        Website : https://huggingface.co/bert-base-uncased 

    """
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    file_path = 'text.txt'

    # opens the file and reads the text inside
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    """
        text.lower()         => converts the texts into lower case 
        tokenizer.encode()   => helps to break down text and give them a unique integer number. 
        tokernizer.decode()  => converts the list of integer indices back into a string 
    """
    tokens = tokenizer.tokenize(
        tokenizer.decode(tokenizer.encode(text.lower())))

    """
        Counter to count the occurance of each unique token. 
    """
    word_counts = Counter(tokens)

    print(word_counts)

    """
        Most common is a function in Counter library taht will help to finds repeated occurance of the token. 
    """
    top_30 = word_counts.most_common(30)

    print("TOP THIRTY WORDs")
    print(top_30)


if __name__ == '__main__':
    count()
