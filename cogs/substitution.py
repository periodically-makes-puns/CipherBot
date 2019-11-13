import quote
import random
from data import db
import discord
from discord.ext import commands
from string import ascii_lowercase

def makeKey():
    alphabetlist = list(ascii_lowercase)
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
        db.writeplaintext(ctx.message.author.id, plaintext)
    
    @commands.command()
    async def patistocrat(self,ctx):
        plaintext = quote.getQuote()
        key = makeKey()
        keyMap = dict(zip(alphabet, key))
        ciphertext = ''.join(keyMap.get(c.lower(), c) for c in plaintext).replace(" ", "")

        await ctx.send(f'Ciphertext: {ciphertext}')
        db.writeplaintext(ctx.message.author.id, plaintext)

def setup(bot):
    bot.add_cog(Substitution(bot))
