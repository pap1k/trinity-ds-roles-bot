import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

RADIO_CHANNEL = 997523978111438888
BOTS_ID = [282859044593598464, 819457016774656060, 797889731731783711, 614109280508968980, 159985870458322944]


@client.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    role = client.get_guild(530673741705904150).get_role(1014517727790121030)
    
    if member.id in BOTS_ID:
        return

    if after.channel != None: #зашел
        if len(after.channel.members) == 1:
            await member.add_roles(role)
        else:
            for mem in after.channel.members:
                await mem.remove_roles(role)
        if before.channel:
            if len(before.channel.members) == 1:
                await before.channel.members[0].add_roles(role)

    else:
        if len(before.channel.members) == 1:
            await before.channel.members[0].add_roles(role)
        await member.remove_roles(role)

@client.event
async def on_ready():
    print(f'Looget in as {client.user}')

client.run(os.getenv("DISCORD_CC"))