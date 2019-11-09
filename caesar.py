import quote
import random

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

def encrypt():
    plaintext = quote.getQuote()
    ciphertext = ""
    shift = random.randint(0,25)

    for l in list(plaintext):
        if ('a' <= l <= 'z'):
             ciphertext += chr((((ord(l) - 97) + shift) % 26)+97)

        if('A' <= l <= 'Z'):
            ciphertext += chr((((ord(l) - 65) + shift) % 26)+65)

        if(l in punctuations):
            ciphertext += l
    
    return [plaintext,ciphertext]

if __name__ == '__main__':
    print(encrypt())