from discord.ext import commands
from discord import app_commands
import discord


class warn_commands(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.has_permissions(kick_members=True)
    @app_commands.command(name="warn", description="Warn a user for rule violations. The warning is logged for moderation purposes.")
    @app_commands.describe(
        user="The user to warn",
        reason="Reason for the warning"
        )
    async def warn(self,interaction:discord.Interaction,user:discord.Member,reason:str =""):
        admin=interaction.user.name
        if reason != "":
            await interaction.response.send_message(f"Admin: `{admin}`\nWarned user: `{user}` -> ID: ||{user.id}||\nReason: {reason}")
            await user.send(f"You have been warned by: `{admin}`\nReason: `{reason}`")
        else:
            await interaction.response.send_message(f"Admin: `{admin}`\nWarned user: `{user}` -> ID: ||{user.id}||")
            await user.send(f"u have been warned from: `{admin}`")


async def setup(bot):
    await bot.add_cog(warn_commands(bot))



