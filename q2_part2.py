s = '56aAww1984sktr235270aYmn145ss785fsq31D0'

number_string = ""
letter_string = ""
ASCII_number = []
ASCII_letter = []
for char in s:
    if char.isalpha():
        letter_string += char
    else:
        number_string += char
for char in letter_string:
    if char.isupper():
        ASCII_letter.append(ord(char))
for char in number_string:
    if int(char) % 2 == 0:
        ASCII_number.append(ord(char))

print(ASCII_letter)
print(ASCII_number)