import quote
import random

plaintext = ""

def makeKey():
   alphabet = list('abcdefghijklmnopqrstuvwxyz')
   random.shuffle(alphabet)
   return ''.join(alphabet)

def aristocrat():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = quote.getQuote()
    key = makeKey()
    keyMap = dict(zip(alphabet, key))
    ciphertext = ''.join(keyMap.get(c.lower(), c) for c in plaintext)

    return [plaintext, ciphertext]

def patistocrat():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = quote.getQuote()
    key = makeKey()
    keyMap = dict(zip(alphabet, key))
    ciphertext = ''.join(keyMap.get(c.lower(), c) for c in plaintext).replace(" ", "")

    return [plaintext, ciphertext] 
