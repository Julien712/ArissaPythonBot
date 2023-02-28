import discord
import random
import asyncio

client = discord.Client(intents=discord.Intents.all())

channel_name = 
message_id = 
role_name = 
reaction_emoji = "✅"

# Liste des statut à afficher
statuses = ["&help", "&play"]


async def change_status():
    while True:
        # Changer le statut toutes les 5 secondes
        for status in statuses:
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=(status)))


@client.event
async def on_ready():
    print(client.user.name, 'est prêt!!')
    print('-----')
    # Démarrer la boucle de changement de statut
    await change_status()
    # obtient le channel à partir de son nom
    channel = guild.get_role(role_name)
    # obtient le message à partir de son ID
    message = await channel.fetch_message(message_id)
    # ajoute la réaction au message
    await message.add_reaction(reaction_emoji)


# ID du channel de bienvenue
channel_id = 

# Envoie des messages de bienvenue lorsque qu'un membre rejoint le serveur
@client.event
async def on_member_join(member):
    try:
        channel = client.get_channel(channel_id)
        avatar_url = member.avatar_url
        title = f"{member} a rejoint le serveur. Nous sommes désormais {member.guild.member_count} ! 🎉"
        embed = discord.Embed(
            title=title, description="N'oublie pas de lire les règles dans <#id> pour un accès total au serveur",
            color=random.randint(0, 0xffffff))
        embed.set_image(avatar_url)
        await channel.send(f"{member}", embed=embed)
    except Exception as e:
        print("An error occurred:", e)


@client.event
async def on_raw_reaction_add(payload):
    # vérifie si la réaction a été ajoutée au bon message
    if payload.message_id == message_id:
        # obtient le membre qui a ajouté la réaction
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        # vérifie si la réaction ajoutée est celle attendue
        if str(payload.emoji) == reaction_emoji:
            # obtient le rôle à partir de son nom
            role = discord.utils.get(guild.roles, name=role_name)
            # ajoute le rôle au membre
            await member.add_roles(role)

# Token permettant la connexion au bot
client.run(
    "TOKEN")
