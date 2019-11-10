import quote
import random
import discord
from discord.ext import commands

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

class Caesar(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def caesar(self,ctx):
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
        
        await ctx.send(f'Ciphertext: {ciphertext}')
        #TODO: Store plaintext in database
        return [plaintext,ciphertext]

def setup(bot):
    bot.add_cog(Caesar(bot))

if __name__ == '__main__':
    print(Caesar.caesar())