import quote
import random
import discord
from discord.ext import commands

plaintext = ""
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def makeKey():
    global alphabet
    alphabetlist = list(alphabet)
    random.shuffle(alphabetlist)
    return ''.join(alphabetlist)

class Substitution(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def aristocrat(self,ctx):
        plaintext = quote.getQuote()
        key = makeKey()
        keyMap = dict(zip(alphabet, key))
        ciphertext = ''.join(keyMap.get(c.lower(), c) for c in plaintext)

        await ctx.send(f'Ciphertext: {ciphertext}')
        #TODO: Store plaintext in database
        return [plaintext, ciphertext]
    
    @commands.command()
    async def patistocrat(self,ctx):
        plaintext = quote.getQuote()
        key = makeKey()
        keyMap = dict(zip(alphabet, key))
        ciphertext = ''.join(keyMap.get(c.lower(), c) for c in plaintext).replace(" ", "")

        await ctx.send(f'Ciphertext: {ciphertext}')
        #TODO: Store plaintext in database
        return [plaintext, ciphertext] 

def setup(bot):
    bot.add_cog(Substitution(bot))
