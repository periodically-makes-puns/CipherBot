import discord
from discord.ext import commands
from data import db
from operator import itemgetter

class Scoreboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def scoreboard(self,ctx):
        scores = db.readallscores()
        scores.sort(key = itemgetter(1), reverse = True)
        if len(scores) < 5:
            await ctx.send("Not enough people have played yet for a leaderboard to form")
            exit()
        else:
            scores = scores[:5]
            await ctx.send(f'```1. {ctx.bot.fetch_user(scores[0][0]).name}\n2. {ctx.bot.get_user(scores[1][0]).name}\n3. {ctx.bot.get_user(scores[2][0]).name}\n4. {ctx.bot.get_user(scores[3][0]).name}\n5. {ctx.bot.get_user(scores[4][0]).name}\n```')

def setup(bot):
    bot.add_cog(Scoreboard(bot))