"""Gname, nick files"""

# Discord
import discord
from discord.ext import commands
# Utils
from utils import read_owners, get_data


class Guild(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['name', 'Change_name'])
    async def change_name(self, ctx):
        await ctx.message.delete()
        guild = ctx.guild
        try:
            await guild.edit(name=get_data('guild_name'))
        except:
            pass


    @commands.command(aliases=['nicks', 'Change_nicks'])
    async def change_nicks(sekf, ctx):
        await ctx.message.delete()
        guild = ctx.guild
        nick = get_data('nick_name')
        for member in guild.members:
                try:
                    if member.id in read_owners():
                        continue
                    else:
                        await member.edit(nick=nick)
                        print(f'{member} username changed to {nick}')
                except:
                    print(f'{member} username cant be changed to {nick}')
                    continue
        

def setup(bot):
    bot.add_cog(Guild(bot))