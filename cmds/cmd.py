from discord.ext import commands
from discord import app_commands
import random
import discord

class mycommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,message:discord.Message):
        if message.content.find("baby") != -1 and not message.author.bot:
            await message.add_reaction("🧡")

    @app_commands.command(name="ping" , description="send pong")
    async def ping(self,interaction:discord.Interaction):
        await interaction.response.send_message("pong",ephemeral=True)

    @app_commands.command()
    async def hello(self,interaction:discord.Interaction):
        await interaction.response.send_message("Hi baby!")

    @commands.command()
    async def say(self,ctx,what="what i say baby?"):
        await ctx.send(what)

    @commands.command()
    async def say2(self,ctx, *what):
        await ctx.send(" ".join(what))

    @commands.command()
    async def say3(self,ctx,what="what i say baby?",why="why?"):
        await ctx.send(what + why)
        
    @commands.command()
    async def choix(self,ctx,*option):
        await ctx.send(random.choice(option)+"<3")

    @commands.command()
    async def math(self,ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"No,{ctx.subcommand_passed} does not be long to math")

    @app_commands.command()
    async def count(self,interaction:discord.Interaction,one:int,two:int):
        await interaction.response.send_message(one + two)

    @commands.command()
    async def min(self,ctx,one:int,two:int):
        await ctx.send(one - two)

    @commands.command()
    async def name(self,ctx,who:discord.Member):
        await ctx.reply(str(who) +" "+ str(who.id))
        
    @commands.command()
    async def join(self,ctx,who:discord.Member):
        await ctx.reply(f"{who} join at {who.joined_at}")
        
    @commands.command(aliases=["av"])
    async def avatar(self,ctx,who:discord.Member):
        await ctx.reply(who.avatar)

    @commands.command(aliases=['dm'])
    @commands.has_role(1290411720791294093)
    async def direct_message(self,ctx,who:discord.Member,*message):
        await who.send((" ").join(message))
        await ctx.send("recived📩")
    @direct_message.error
    async def direct_message_error(self,ctx,error):
        if isinstance(error,commands.CommandError):
            await ctx.send(f"u need role `{ctx.guild.get_role(1290411720791294093).name}`")
    
    

async def setup(bot):
    await bot.add_cog(mycommands(bot))
