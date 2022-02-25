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
    kantutan = ["sex", "torjack", "kantot"]
    words=str.lower(ctx.content)
    if words in kantutan:
        user=ctx.author
        voice_channel = user.voice.channel
        await voice_channel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild= ctx.guild)
        voice.play(discord.FFmpegPCMAudio("audio/sex.mp3"))
        while voice.is_playing():
            time.sleep(.1)
        await voice.disconnect()
    
    
def setup(bot):
  bot.add_cog(Sex(bot))