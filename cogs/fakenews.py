import discord
from discord.ext import commands
import time
bot = discord.Client()
class Sex(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener() # In cogs, to listen for events use .Cog.listener
  async def on_message(self, ctx): # You must not forget to pass "self" as the first parameter for functions inside classes.
    # We don't use "bot.something", we use "self.bot.something" in cogs.
    
    words=str.lower(ctx.content)
    if "totoo" in words:
       await ctx.send("https://cdn.discordapp.com/attachments/849185224221786132/975583785741602816/asd.png")
    
    
def setup(bot):
  bot.add_cog(Sex(bot))