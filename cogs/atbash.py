import quote
from data import db
import discord
from discord.ext import commands

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

class Atbash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def atbash(self, ctx):
        ciphertext = ""
        plaintext = quote.getQuote()
        for l in plaintext:
            if ('a' <= l <= 'z'):
                ciphertext += chr(122 - ord(l) + 97)
            
            if('A' <= l <= 'Z'):
                ciphertext += chr(90 - ord(l) + 65)

            if (l in punctuations):
                ciphertext += l
        
        await ctx.send(f'Ciphertext: {ciphertext}')
        db.writeplaintext(ctx.message.author.id, plaintext)

def setup(bot):
    bot.add_cog(Atbash(bot))

if __name__ == '__main__':
    print(Atbash.atbash())