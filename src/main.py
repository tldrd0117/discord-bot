import discord
from dotenv import dotenv_values

client = discord.Client()
config = dotenv_values('.env')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    ch = client.get_channel(int(config["CHANNEL"]))
    await ch.send("i wanna go home")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(config["TOKEN"])