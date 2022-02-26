from discord.ext import commands
class EnterChannelGreetings(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener() # In cogs, to listen for events use .Cog.listener
  async def on_voice_state_update(self, member, before, after):
    nagUndeaf = before.self_deaf and not after.self_deaf
    nagUnmute = before.self_mute and not after.self_mute
    nagtanggalNgStream = before.self_stream and not after.self_stream
    nagtanggalNgVideo = before.self_video and not after.self_video

    # ignore nagUndeaf / nagUnmute
    if nagUndeaf or nagUnmute:
        return

    # ignore nagDeaf / nagMute
    if after.self_deaf or after.self_mute:
        return

    # ignore nagstream / nag-tanggal ng stream
    if after.self_stream or nagtanggalNgStream:
        return

    # ignore nagturn-on ng video cam / nagtanggal ng video cam
    if after.self_video or nagtanggalNgVideo:
        return
    
    # ignore yung umalis ng Channel malamang tanga ka ba
    if after.channel == None:
        return
    
    # don't greet a bot
    if member.bot: 
        return

    channel_found = None

    # TODO: Repeating code na. Dapat nasa hiwalay na method na to.
    if after.channel.name == "BoysLockerRoom":
      for channel in member.guild.channels:
        if channel.name == 'private-chat':
          channel_found = channel
          await channel_found.send(f"Welcome to {after.channel.name} {member.mention}")
          break
    
    if after.channel.name == "Extreme High Council":
      for channel in member.guild.channels:
        if channel.name == 'council-chat':
          channel_found = channel
          await channel_found.send(f"Welcome to {after.channel.name} {member.mention}")
          break
    
    # if after.channel.name.__contains__("Ranked ng Smurf"):
    #   for channel in member.guild.channels:
    #     if channel.name.__contains__("main-chat"):
    #       channel_found = channel
    #       await channel_found.send(f"Welcome to {after.channel.name} {member.mention} stream mo naman lods sayang boost")
    #       break

    
def setup(bot):
  bot.add_cog(EnterChannelGreetings(bot))