#id 763972228814471178
#permission interger 75840

import discord
import sys
import re

#code = "ABCDEF"
client = discord.Client()
#user = discord.User()
token = open("token.txt", "r").read()

def statuses(guild):
    online = 0
    offline = 0
    idle = 0
    dnd = 0

    for m in guild.members:
        if str(m.status) == "online":
            online += 1
        elif str(m.status) == "offline":
            offline += 1
        elif str(m.status) == "idle":
            idle += 1
        else :
            dnd += 1
    
    return (online, offline, idle, dnd)

temp = "ABCDEF"
def save_code(code):
    global temp
    temp = code

@client.event       #event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    print(f"{message.channel} : {message.author} : {message.author.name} : {message.content}")

    global guild
    guild = client.get_guild(763848351183536128)

    if message.author == client.user:
        return

    if ("hello" or "hello mia") == message.content.lower() or ("hi" or "hi mia") == message.content.lower() or ("hey" or "hey mia" or "hey bot mia") == message.content.lower():
        await message.channel.send('Hey.')

    if "!command" in message.content.lower():
        await message.channel.send(f" ```All the commands must be followed by the '!' symbol``` \n 1. mia - Who am I? \n 2. code - Shows the code for current game \n 3. srijani - surpirse\n 4. reshma - surprise x2 \n 5. member - Display the member count \n 6. status - Current status of all the members (not the single one obv, lol)") 
    
    if "!mia" in message.content.lower():
        await message.channel.send("Hey! I am Mia. How can I help you? To interact with me, type '!commands'")
    
    elif "!member" in message.content.lower():
        await message.channel.send(f"```{guild.member_count}```")

    elif "!status" in message.content.lower():
        (on, off, idlee, dond) = statuses(guild)
        await message.channel.send(f"```online : {on}, offline : {off}, idle : {idlee}, do-not-disturb : {dond}, invisible : :)_stupid_```")

    elif "among us" in message.content.lower() or "umang us" in message.content.lower():
        await message.channel.send("Oh yeah!! I am in.")

    elif "!logout" in message.content.lower():
        await message.channel.send("This option has been changed lately by the owner. If you think it's a mistake, contact the owner.")
        # await client.close()
        # sys.exit()

    if(message.mention_everyone):
        await message.channel.send("hmm.. everyone is mentioned but why...?")

    l = message.mentions
    for i in l:
        await message.channel.send(f"{i} mentioned and detected...")

    if "!bot" in message.content.lower():
        l = guild.members
        for i in l:
            await message.channel.send(f" I am {i}. I am here to help you, type !commands for more options")
    
    mssg = message.content
    if mssg == mssg.upper() and len(mssg) == 6:
        global code
        code = mssg
        save_code(code)
        await message.channel.send("Code detected and saved")
    
    if "!code" in message.content.lower():
        await message.channel.send(f"The code is: {code}. Have a nice game!")

    # if re.findall("^hello|hey|hi", message.content.lower()):
    #     await message.channel.send(f"Hey {message.author.name}!")
    
    # if re.findall("^!find", message.content.lower()):
    #     return
    
@client.event
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to Umang Us server!')

@client.event
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

client.run(token)


