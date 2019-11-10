import quote
import random
from string import punctuation

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

def morse(plaintext): 
    morsecode = ''
    plaintext = plaintext.translate(str.maketrans('', '', punctuation))

    for letter in plaintext.upper():
        if letter == ' ': 
            morsecode += " "
        else:
            morsecode += MORSE_CODE_DICT[letter] + ' '

    return morsecode

def pollux():
    plaintext = quote.getQuote()
    morsecode = morse(plaintext.upper()).replace(" ", "x")
    # morsecode always has an x at the end? Should it be like this?
    digitsymbols = ["x","-","."]
    key = [random.choice(digitsymbols) for i in range(9)]
    ciphertext = ""

    for n in morsecode:
        ciphertext += str(random.choice([i for i, x in enumerate(key) if x == n]))
    
    ciphertext = ' '.join([ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)])
    
    for i in range(random.randint(0,3)):
        key[key.index(random.choice(key))] = "?"

    return [plaintext,ciphertext,key]