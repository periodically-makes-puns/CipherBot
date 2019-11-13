import quote
import random
from string import punctuation
from data import db
import discord
from discord.ext import commands

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

class Morse(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def pollux(self,ctx):
        plaintext = getQuote()
        morsecode = morse(plaintext.upper().strip()).replace(" ", "x")
        # morsecode always has an x at the end? Should it be like this?
        digitsymbols = ["x","-","."]
        key = list("....---xxx")
        random.shuffle(key)
        ciphertext = ""

        for n in morsecode:
            ciphertext += str(random.choice([i for i, x in enumerate(key) if x == n]))

        ciphertext = ' '.join([ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)])

        if random.random() > 0.5:
            for i in range(random.randint(0,4)): # give 6 of key
                key[key.index(random.choice(key))] = "?"
            crib = None
        else:
            sind = random.randint(0, len(plaintext)-4)
            crib = plaintext[sind:sind+4]

        print(f'Ciphertext: {ciphertext}\n' + (f"Crib: {crib}\n" if crib is not None else f"Key: {''.join(key)}\n"))

def morse(plaintext: str) -> str:
        morsecode = ''
        plaintext = plaintext.translate(str.maketrans('', '', punctuation))

        for letter in plaintext.upper():
            if letter == ' ': 
                morsecode += " "
            else:
                morsecode += MORSE_CODE_DICT[letter] + ' '

        return morsecode[:-1] # remove trailing space

def setup(bot):
    bot.add_cog(Morse(bot))