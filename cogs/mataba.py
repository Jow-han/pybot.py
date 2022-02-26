import discord
from discord.ext import commands
import time
class Mataba(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command() # In cogs, we use @commands.command() and not @bot.command().
  async def mataba(self, ctx): 
    user = ctx.author
    voice_channel = user.voice.channel

    await voice_channel.connect()

    voice = discord.utils.get(self.bot.voice_clients, guild= ctx.guild)
    voice.play(discord.FFmpegPCMAudio("audio/fatfuck.mp3"))

    while voice.is_playing():
      time.sleep(.1)

    await voice.disconnect()
    
def setup(bot):
  bot.add_cog(Mataba(bot))