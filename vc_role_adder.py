from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!')

client = discord.Client()

#BOT TOKEN
TOKEN = 'x'


#ids should be a string of numbers
vc_one, vc_two = 0, 0

@client.event
async def on_ready() -> None:
    print(f'We have logged in as {client}')

# VC PROCESSING
@client.event
async def on_voice_state_update(member, before, after) -> None:
    role = discord.utils.get(member.guild.roles, name="old role")
    current_role = discord.utils.get(member.guild.roles, name="new role")
    await member.remove_roles(role)
    await member.add_roles(current_role)
    
    if not before.channel and after.channel:
        channel_id = member.voice.channel.id
        if channel_id in [vc_one, vc_two]: #== vc_one or channel_id == vc_two:
            await member.add_roles(current_role)
            
    elif before.channel and not after.channel:
        await member.add_roles(role)
        await member.remove_roles(current_role)

client.run(TOKEN)
