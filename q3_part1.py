# THIS CODE IS THE FIRST PART OF QUESTION 3
# The code here decrypts the encrypted code saved in "encrypted_text.txt"
# and saves the decrypted code in "decrypted_code.txt"

def decrypt(text, key):
    """This function decrypts encrypted text"""
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key # reverse operation to encryption
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

total = 0 # total is equivalent to key

for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2

with open("encrypted_text.txt", "r") as file:
    text = file.read()

decrypted_text = decrypt(text, total)

with open("decrypted_text.txt", "w") as file:
    file.write(decrypted_text)

