import discord
from discord.ext import commands
class Dogstyle(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command() # In cogs, we use @commands.command() and not @bot.command().
  async def dogstyle(self, ctx): 
    await ctx.send("https://media.discordapp.net/attachments/819854712576409600/820110846512463882/unknown.png")
    
def setup(bot):
  bot.add_cog(Dogstyle(bot))