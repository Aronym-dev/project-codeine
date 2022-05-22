"""Emojis files"""

# Discord
import discord
from discord.ext import commands
# Utils
from utils import get_data, get_image_file


class Emojis(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

                
    @commands.command(aliases=['ce','c_emojis','emojis','Create_emojis','Create_Emojis','create_Emojis'])
    async def create_emojis(self,ctx):
        """Create 50 emojis with a image"""
        await ctx.message.delete()
        with open('cogs/image.jpg', 'rb') as image:
            image = image.read()
            guild = ctx.guild
            for emoji in range(1, 51):
                try:
                    await guild.create_custom_emoji(name=(str(get_data('emojis_name'))+str(emoji)), image=image)
                    print('Emoji succesfuly created')
                except:
                    print('Emoji cant be created')
                

    @commands.command(aliases=['del_e','d_emojis','del_emojis','Delete_emojis','Delete_Emojis','delete_Emojis'])
    async def delete_emojis(self,ctx):
        """Delete all emojis in the server as possible"""
        await ctx.message.delete()
        guild = ctx.guild
        for emoji in guild.emojis:
            try:
                await emoji.delete()
            except:
                pass
            

def setup(bot):
    bot.add_cog(Emojis(bot))