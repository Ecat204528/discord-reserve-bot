import discord
import re
import sys
from time import sleep

client = discord.Client()
f = open('token.txt', mode='r')
TOKEN = f.readline()


@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

@client.event
async def on_message(message):

    if message.author.bot:
        return

    if message.content == "call stop":
        sys.exit()

    if re.fullmatch('call\skick\s(n|([sm]\s[0-9][0-9][0-9]))', message.content) != None:
        print("is match")
        talk_channel_id = 795982514664767522
        channel = client.get_channel(talk_channel_id)
        o = message.content[10]
        if o != 'n':
            if o == 's':
                u = 1
            elif o == 'm':
                u = 60
            t = int(message.content[12:15])
            sleep_time = t * u
            print("sleep ", sleep_time)
            sleep(sleep_time)

        for ch in channel.guild.voice_channels:
            for member in ch.members:
                if member.id == message.author.id:
                    await member.move_to(None)
                    pritn("kick")

client.run(TOKEN)

f.close()
