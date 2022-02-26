import discord
from discord.ext import commands
class Hello(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command() # In cogs, we use @commands.command() and not @bot.command().
  async def hello(self, ctx):
    await ctx.send("hello ka rin")
    
def setup(bot):
  bot.add_cog(Hello(bot))