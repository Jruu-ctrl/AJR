import settings
import discord
import random
from discord.ext import commands

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

        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file.name != "_init__.py":
                await bot.load_extension(f"{cmd_file.name[:-3]}")
    
    @bot.event
    async def on_command_error(ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("eurror globaly")
        


    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__=="__main__":
    run()