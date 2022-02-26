import discord
from discord.ext import commands
import time
class Nigger(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def nigger(self, ctx): 
    user = ctx.author
    voice_channel = user.voice.channel

    await voice_channel.connect()

    voice = discord.utils.get(self.bot.voice_clients, guild= ctx.guild)
    voice.play(discord.FFmpegPCMAudio("audio/nigger.mp3"))

    while voice.is_playing():
      time.sleep(.1)

    await voice.disconnect()
    
def setup(bot):
  bot.add_cog(Nigger(bot))