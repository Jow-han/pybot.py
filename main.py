# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from discord.ext import commands
import random
import time
# Import the os module.
import os
from config import token
# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
# bot = discord.Client()
bot = commands.Bot(command_prefix="")

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id}(name: {guild.name})")
        # INCREMENTS THE GUILD COUNTER
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS/SERVERS THE BOT IS IN
    print("PyBot is in" + str(guild_count) + "guilds.")

    await bot.change_presence(activity=discord.Game(name="Python 3 on VSCode"))

    # Cogs code - start
    for cog in os.listdir(r"cogs"): # Loop through each file in your "cogs" folder.
      if cog.endswith(".py"):
          try:
              cog = f"cogs.{cog.replace('.py', '')}"
              bot.load_extension(cog) # Load the file as an extension.
          except Exception as e:
              print(f"{cog} is failed to load:")
              raise e
    # Cogs code - end



#EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    # changes message content into lowercase
    words=str.lower(message.content)
    #grab the user who sent the command
    user = message.author
    voice_channel = user.voice.channel
        
        #voiceChannel = discord.utils.get(message.guild.voice_channels, name = voice_channel)
        #voice = discord.utils.get(bot.voice_clients, guild=message.guild)
        
        
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'Cool. Cool cool cool cool cool cool cool', 
        'no doubt no doubt no doubt no doubt.'
    ]
    the_office = [
        "Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.",
        "I\'m not superstitious, but I am a little stitious.",
        "The worst thing about prison was the dementors."
    ]
    dead = [
        "https://s.yimg.com/uu/api/res/1.2/27yeB91IS2Vg58yvePUJ9A--~B/aD03Njg7dz0xMDI0O2FwcGlkPXl0YWNoeW9u/http://media.zenfs.com/en-SG/homerun/the_hive_asia_947/9bc64f74c9dcd321e2daa890e112348f",
        "http://assets.rappler.com/C6965FC179534E97B3CC676BBFF1599A/img/7779C656CA9C486EB29364A166236AF8/emmannn.jpg",
        "https://pbs.twimg.com/media/Dxq12kBVAAEwz85.jpg",
        "https://ichef.bbci.co.uk/news/976/cpsprodpb/1344F/production/_116572987_dacerafacebook.jpg",
        "https://www.getrealphilippines.com/wp-content/uploads/2018/05/ninoy_aquino_international_airport-1.jpg",
        "https://cdn.discordapp.com/attachments/849185224221786132/945202027313635408/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f5f7263446536793975585f5f7a773d3d2d3833333930313838322e313565663162313030646362633533643632353031313637373235382e6a7067.png"
    ]
    marcos = [
        "https://cdn.discordapp.com/attachments/849185224221786132/945203028590460978/VZSQOHVYTD4J3PZ4SWMXBHMJPE.png",
        "https://cdn.discordapp.com/attachments/849185224221786132/945202801099800606/marcos.jpg"
    ]
    commands = [
        "dead","gelo cruz","the office","dead","cake","depressed"
    ]
    try:
        if words == '99!':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)
        # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
        if words == "hello":
            # SENDS BACK A MESSAGE TO THE CHANNEL.
            await message.channel.send("hello ka rin")
        elif words == "best porn producer in ph":
            await message.channel.send("Vivamax films")
        elif "ayun" in words:
            await message.channel.send("Ahyun")
        elif words == "gelo cruz":
            await message.channel.send("Yung matabang tomboy na nangaway ng bata sa McDo sa Pasig")
            time.sleep(1.5)
            await voice_channel.connect()
            voice = discord.utils.get(bot.voice_clients, guild=message.guild)
            voice.play(discord.FFmpegPCMAudio("audio/gelocruz.mp3"))
            time.sleep(6)
            await voice.disconnect()
            return
        if "low ranks" in words:
            await message.channel.send("Low rank ka naman" + message.author.mention)
        if "need" in words:
            await message.channel.send("Need mo ng susubo ng burat?")
        elif words == "the office":
            theofficeresponse = random.choice(the_office)
            await message.channel.send(theofficeresponse)
        elif "pagsamo" in words:
            await message.channel.send("tama na please")
        elif "kain" in words:
            await message.channel.send("kain ka burat")
        elif message.content.startswith('wait'):
            await message.channel.send('tagal ohh tanginang to')   
        elif words == "dead" or words == "yataps":
            deadresponse = random.choice(dead)
            await message.channel.send(deadresponse)
        elif words == "cake" or words == "lodicakes":
            marcoslodicake = random.choice(marcos)
            await message.channel.send(marcoslodicake)
        elif "depressed" in words:
            await message.channel.send("https://c.tenor.com/rv_QpUUUW0sAAAAC/dwight-the-office.gif")
        elif words == "command list" or words == "pybot commands":
            await message.channel.send(commands)
        elif words == 'dogstyle':
            await message.channel.send("https://media.discordapp.net/attachments/819854712576409600/820110846512463882/unknown.png")
        elif 'wag' in words:
            await message.channel.send("https://images-ext-2.discordapp.net/external/rMF7uHkVpovUDZTQnHo4XAfudHHZHigLYJPa8ZW3Q98/https/i.pinimg.com/236x/c6/49/eb/c649eb07789ec9794983101fca8b01e7.jpg")
        elif words == 'happy new year':
                user=message.author
                voice_channel = user.voice.channel
                await voice_channel.connect()
                voice = discord.utils.get(bot.voice_clients, guild=message.guild)
                voice.play(discord.FFmpegPCMAudio("audio/happynewyear.mp3"))
                time.sleep(15)
                await voice.disconnect()
                return
        elif words == "bully":
            user=message.author
            voice_channel = user.voice.channel
            await voice_channel.connect()
            voice = discord.utils.get(bot.voice_clients, guild=message.guild)
            voice.play(discord.FFmpegPCMAudio("audio/gonnacry.mp3"))
            time.sleep(4)
            await voice.disconnect()
            return
        elif words == "gameon":
            user=message.author
            voice_channel = user.voice.channel
            await voice_channel.connect()
            voice = discord.utils.get(bot.voice_clients, guild=message.guild)
            voice.play(discord.FFmpegPCMAudio("audio/gaymoan.mp3"))
            time.sleep(7)
            await voice.disconnect()
            return
        elif words == "mataba":
            user=message.author
            voice_channel = user.voice.channel
            await voice_channel.connect()
            voice = discord.utils.get(bot.voice_clients, guild=message.guild)
            voice.play(discord.FFmpegPCMAudio("audio/fatfuck.mp3"))
            time.sleep(7)
            await voice.disconnect()
            return
        elif words == "nigger":
            user=message.author
            voice_channel = user.voice.channel
            await voice_channel.connect()
            voice = discord.utils.get(bot.voice_clients, guild=message.guild)
            voice.play(discord.FFmpegPCMAudio("audio/nigger.mp3"))
            time.sleep(7)
            await voice.disconnect()
            return
        elif words == "focus":
            user=message.author
            voice_channel = user.voice.channel
            await voice_channel.connect()
            voice = discord.utils.get(bot.voice_clients, guild=message.guild)
            voice.play(discord.FFmpegPCMAudio("audio/dimakafocus.mp3"))
            time.sleep(4)
             # Sleep while audio is playing.
            while voice.is_playing():
                sleep(.1)
            await voice.disconnect()
            return

            
        # need to add this await command so Cog Commands can work.
        # Without this, Cog Commands gets blocked.
        # Source: https://stackoverflow.com/a/53706211/7209628
        await bot.process_commands(message)
    except:
         await message.channel.send(message.author.mention + ', Teka error ako help')


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. 
bot.run(token)

