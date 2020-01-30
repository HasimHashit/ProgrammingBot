import discord
import logging
token = "NjcyMzk4MDg2MjE5NDk3NDgy.XjK5xg.0WKeZYNHTn-GQ08joJ-b_-Vq83w"
client = discord.Client()




@client.event
async def on_message(message):
    print(message.author, message.content)
    if message.content == "!hello":
       await message.channel.send("Hello")


client.run(token)



