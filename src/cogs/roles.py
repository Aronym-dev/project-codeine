"""Roles file"""

# Discord
import discord
from discord.ext import commands

from utils import get_data

class Roles(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(aliases=['cr', 'CR', 'create_role', 'roles_create', 'role_create'])
    async def create_roles(self, ctx):
        """Create the roles with the name defined by the user"""
        await ctx.message.delete()
        guild = ctx.guild
        for role in range(50):
            try:
                await guild.create_role(name=get_data('role_name'))
            except:
                pass
    
    
     
    @commands.command(aliases=['dr','DR', 'delete_role', 'roles_delete', 'role_delete'])
    async def delete_roles(self, ctx):
        """Delete all the roles that are in the discord's server"""
        await ctx.message.delete()
        guild = ctx.message.guild
        for role in guild.roles:
            try:
                await role.delete()
            except:
                pass
        
    
def setup(bot):
    bot.add_cog(Roles(bot))