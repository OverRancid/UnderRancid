import discord
import os
import json
from discord.ext import commands

client = commands.Bot(command_prefix = "~")

@client.event
async def on_ready():
    print(f'\n\nBot is ready!\nName: {client.user.name}\nID: {client.user.id}\n      ---------\n')

    return

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded {filename[:-3]}')

@client.event
async def on_guild_join(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '~'

    with open('prefixes.json','w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json','w') as f:
        json.dump(prefixes, f, indent=4)

@commands.has_permissions(administrator = True)
@client.command()
async def prefix(ctx , prefix):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json','w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send("Changed server prefix to " + prefix)

client.run('NzQxMjk2NjAzNzMzOTUwNDk0.Xy1gQg.9JJre7psWNstT0pv-H5lrYeZ_wA')
