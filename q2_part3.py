# This program uses a key to decrypt text

def decrypt(text, key):
    """This function decrypts encrypted text using a key"""
    
    decrypted_text = "" # declare variables

    for char in text: # iterate through each character
        
        if char.isalpha(): # if character is a letter we implement decryption process
            shifted = ord(char) - key # reverse operation to encryption
            
            if char.islower(): # decrypt lowercase letters outside bounds
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26

            elif char.isupper(): # decrypt uppercase letters outside bounds
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)

        else: # if character is not a letter, it does not need to be decrypted
            decrypted_text += char

    return decrypted_text

text = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGHXRF V NZ BHG BS PBAGEBY \n NAQNG GVZRF GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF \n URYYGBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
s = 13 # shift key is 13

print(decrypt(text, s))