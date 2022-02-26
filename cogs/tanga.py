import discord
from discord.ext import commands
class Tanga(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command() # In cogs, we use @commands.command() and not @bot.command().
  async def tanga(self, ctx): # You must not forget to pass "self" as the first parameter for functions inside classes.
    # We don't use "bot.something", we use "self.bot.something" in cogs.
    await ctx.send("tanga mo") 
    
def setup(bot):
  bot.add_cog(Tanga(bot))