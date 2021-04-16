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

    if re.fullmatch('call\skick\s([0-9][0-9][0-9]|(now))', message.content) != None:
        print("is match")
        talk_channel_id = 795982514664767522
        channel = client.get_channel(talk_channel_id)
        #ToDo パラメータ解析-文字列の加工
        s = message.content[10:13]
        #ToDo 解析結果をもとに時間調整-一定時間後に先に進む
        if s == "now":
            i = 0
        else:
            i = int(s)

        sleep_time = i * 60
        print("sleep ", i, " sec")
        sleep(sleep_time)

        for ch in channel.guild.voice_channels:
            for member in ch.members:
                if member.id == message.author.id:
                    await member.move_to(None)

client.run(TOKEN)

f.close()
