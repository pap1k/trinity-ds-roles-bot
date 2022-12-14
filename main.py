import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

RADIO_CHANNEL = 997523978111438888

def countUsers(channel):
    c = 0
    if channel and channel.members:
        for mem in channel.members:
            if not mem.bot:
                c += 1
    return c

def getUser(channel : discord.channel) -> discord.Member:
    for mem in channel.members:
        if not mem.bot:
            return mem
    return None

@client.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    role = client.get_guild(530673741705904150).get_role(1014517727790121030)
    
    if after.self_mute:
        await member.add_roles(role)
    else:
        await member.remove_roles(role)

    if member.bot:
        return

    if after.channel != None: #зашел
        if countUsers(after.channel) == 1 or after.self_mute:
            await member.add_roles(role)
        else:
            for mem in after.channel.members:
                if not mem.voice.self_mute:
                    await mem.remove_roles(role)
        if before.channel:
            if countUsers(before.channel) == 1:
                await getUser(before.channel).add_roles(role)

    else:
        if countUsers(before.channel.members) == 1:
            await getUser(before.channel).add_roles(role)
        await member.remove_roles(role)

@client.event
async def on_ready():
    print(f'Looget in as {client.user}')

client.run(os.getenv("DISCORD_CC"))