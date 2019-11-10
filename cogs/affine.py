import quote
import random

a_vals = [1, 3, 5, 7, 9, 11 ,15, 17, 19, 21, 23, 25]
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

def encrypt():
    a = random.choice(a_vals)
    b = random.randint(0,25)
    ciphertext = ""
    plaintext = quote.getQuote()
    
    for l in plaintext:
        if 'a' <= l <= 'z':
            ciphertext += chr(((a*(ord(l)-97) + b) % 26) + 97)
        if 'A' <= l <= 'Z':
            ciphertext += chr(((a*(ord(l)-65) + b) % 26) + 65)
        if l in punctuations:
            ciphertext += l
    
    return [plaintext,ciphertext,a,b]

if __name__ == '__main__':
    print(encrypt())