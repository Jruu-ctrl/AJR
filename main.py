import settings
import discord
import random
from discord.ext import commands
from discord import app_commands

logger = settings.logging.getLogger("bot")

def run():
    intents=discord.Intents.default()
    intents.message_content= True
    
    bot = commands.Bot(command_prefix="!",intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"user:{bot.user}(ID:{bot.user.id})")
        print(bot.user)
        print(bot.user.id)

        for file in settings.CMDS_DIR.glob("*.py"):
            await bot.load_extension(f"cmds.{file.name[:-3]}")
        
        bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        await bot.tree.sync(guild=settings.GUILDS_ID)

    @bot.tree.command()
    async def reload(interaction:discord.Interaction,file:str):
        await bot.reload_extension(f"cmds.{file.lower()}")
        await interaction.response.send_message(f"✅Successfully reloaded {file}")

    @bot.tree.error
    async def on_app_command_error(interaction:discord.Interaction,error):
        if isinstance(error,app_commands.CommandInvokeError):
            await interaction.response.send_message("eurror globaly",ephemeral=True)
        


    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__=="__main__":
    run()