import settings
import discord
from discord.ext import commands
from discord import app_commands

logger = settings.logging.getLogger("bot")

def run():
    intents=discord.Intents.default()
    intents.message_content= True
    
    bot = commands.Bot(command_prefix="!",intents=intents,help_command=None)
    
    @bot.event
    async def on_ready():
        logger.info(f"user:{bot.user}(ID:{bot.user.id})")
        print(r"""
            _       _ ____  
           / \     | |  _ \ 
          / _ \ _  | | |_) |
         / ___ \ |_| |  _ < 
        /_/   \_\___/|_| \_\
								""")
        print(bot.user)
        print(bot.user.id)

        for file in settings.CMDS_DIR.glob("*.py"):
            await bot.load_extension(f"cmds.{file.name[:-3]}")

        await bot.tree.sync()

    @bot.tree.context_menu(name="Join")
    async def join(interaction:discord.Interaction, member:discord.Member):
        await interaction.response.send_message(f"`{member.name}` joined on `{member.joined_at.strftime("%Y/%m/%d %H-%M-%S")}`", ephemeral=True)


    @bot.tree.command(description="Module refresh initiated")
    @app_commands.describe(module="Module to refresh:")
    async def reload(interaction:discord.Interaction,module:str):
        if interaction.user.id == 1231632325062950922 :
            await bot.reload_extension(f"cmds.{module.lower()}")
            await interaction.response.send_message(f"Successfully reloaded **{module}** 🪐",ephemeral=True)
        else:
            await interaction.response.send_message(f"**only Jruu can use this command 🧸**",ephemeral=True)


    @bot.tree.error
    async def on_app_command_error(interaction:discord.Interaction,error):
        if isinstance(error,app_commands.CommandInvokeError):
            await interaction.response.send_message("The command you entered is incorrect. Please check the syntax and try again.",ephemeral=True)
        


    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__=="__main__":
    run()