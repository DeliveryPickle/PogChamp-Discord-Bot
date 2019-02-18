from keep_alive import keep_alive
import discord
from discord.ext.commands import Bot
import os
import re
import unidecode
import json
activate = False

client = discord.Client()
prefix = ("p!")
client = Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print("Online")
    print(client.user)

@client.command()
async def delete():
  global activate
  activate = True
  await client.say("```Messages will now be deleted```")

@client.command()
async def keep():
  global activate
  activate = False
  await client.say("```Messages will now be kept```")

@client.event
async def on_message(message):
    #print(message.content)
    discordmessage = str(message.content).replace(" ", "")
    discordmessage = unidecode.unidecode(discordmessage)
    discordmessage = re.sub(r'[.|?|/|\||(|)|+|<|>|,|;|:|{|}|*|-|=|#|^|&|~|!|`|_|]', r'', discordmessage)
    global activate

    if (discordmessage.lower()).find('pogchamp') > -1 and message.author != client.user:
      if (activate is True):
        print('test')
        try:
          await client.delete_message(message)
        except:
            pass
      await client.send_message(message.channel, message.author.mention +' You have used the forbidden emote please refrain from doing so')     

    elif (discordmessage.lower()).find('poggers') > -1 and message.author != client.user:
      if (activate is True):
        print('test')
        try:
          await client.delete_message(message)
        except:
            pass
      await client.send_message(message.channel, message.author.mention +' You have used the forbidden emote please refrain from doing so')  

    elif (discordmessage.lower()).find('<:pogchamp:537124386742730768>') > -1 and message.author != client.user:
      if (activate is True):
        print('test')
        try:
          await client.delete_message(message)
        except:
            pass
      await client.send_message(message.channel, message.author.mention +' You have used the forbidden emote please refrain from doing so')

    await client.process_commands(message)

keep_alive()
client.run(str(os.environ.get('BOT_TOKEN')))
