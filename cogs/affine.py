import quote
import random
import discord
from discord.ext import commands

a_vals = [1, 3, 5, 7, 9, 11 ,15, 17, 19, 21, 23, 25]
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

class Affine(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def affine(self, ctx):
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

        await ctx.send(f'Ciphertext: {ciphertext}\nA: {a}\nB: {b}')
        #TODO: Store plaintext in database
        return [plaintext,ciphertext,a,b]

def setup(bot):
    bot.add_cog(Affine(bot))

if __name__ == '__main__':
    print(Affine.affine())