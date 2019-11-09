import quote

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

def encrypt():
    ciphertext = ""
    plaintext = quote.getQuote()
    for l in plaintext:
        if ('a' <= l <= 'z'):
            ciphertext += chr(122 - ord(l) + 97)
        
        if('A' <= l <= 'Z'):
            ciphertext += chr(90 - ord(l) + 65)

        if (l in punctuations):
            ciphertext += l

    return [plaintext,ciphertext]

if __name__ == '__main__':
    print(encrypt())