import discord
from discord.ext import commands
from data import db
from operator import itemgetter

class Scoreboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def scoreboard(self,ctx):
        leaderboard = f'```'
        scores = db.readallscores()
        scores.sort(key = itemgetter(1), reverse = True)
        scores = scores[:5]
        for index, score in enumerate(scores):
            leaderboard += f'\n{index + 1}. {ctx.bot.get_user(score[0]).name} {score}'
        
        leaderboard += f'```'
        await ctx.send(leaderboard)

def setup(bot):
    bot.add_cog(Scoreboard(bot))
