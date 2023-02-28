import discord
import asyncio

client = discord.Client()


channel_1_id = "CHANNEL_ID"
channel_2_id = "CHANNEL_ID"


@client.event
async def on_voice_state_update(member, before, after):
    # vérifie si l'utilisateur est entré dans un channel vocal
    if before.channel is None and after.channel is not None:
        # vérifie si l'utilisateur est entré dans l'un des channels définis
        if after.channel.id == channel_1_id or after.channel.id == channel_2_id:
            # déplace l'utilisateur de manière répétée entre les deux channels
            while True:
                await member.move_to(client.get_channel(channel_1_id))
                await asyncio.sleep(10)
                await member.move_to(client.get_channel(channel_2_id))
                await asyncio.sleep(10)


@client.event
async def on_voice_state_update(member, before, after):
    # vérifie si l'utilisateur est entré dans un channel vocal
    if before.channel is None and after.channel is not None:
        # vérifie si l'utilisateur est entré dans l'un des channels définis
        if after.channel.id == channel_1_id or after.channel.id == channel_2_id:
            # déplace l'utilisateur de manière répétée entre les deux channels
            while True:
                await member.move_to(client.get_channel(channel_1_id))
                await asyncio.sleep(10)
                await member.move_to(client.get_channel(channel_2_id))
                await asyncio.sleep(10)

# remplacez TOKEN par le token de votre bot
client.run("TOKEN")