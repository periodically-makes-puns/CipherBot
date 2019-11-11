import discord
from discord.ext import commands
from data import db
from string import punctuation

class Check(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def check(self, ctx):
        userid = ctx.message.author.id
        response = ctx.message.content[8:].translate(str.maketrans('', '', punctuation))
        ans = db.readplaintext(userid)
        
        if(ans == ""):
            await ctx.send("Ask me to give you a cipher problem first.")
        
        elif(response == ""):
            await ctx.send("You need to give me an answer silly!")
        
        elif(ans.lower().translate(str.maketrans('', '', punctuation)) == response.lower()):
            await ctx.send(f'Correct!\nPlaintext: ||{ans}||')
            db.writeplaintext(userid,"")
        
        elif(ans.lower().translate(str.maketrans('', '', punctuation)) != response.lower()):
            await ctx.send(f'Wrong.\nPlaintext: ||{ans}||')
            db.writeplaintext(userid,"")

def setup(bot):
    bot.add_cog(Check(bot))
