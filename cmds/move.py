from discord.ext import commands
from discord import app_commands
import discord
from datetime import timedelta

class move_command(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @app_commands.command(name="move",description="move so to x channel.")
    @app_commands.describe(
        member="The user to move",
        channel="to chanel")
    async def move(self,
                   interaction:discord.Interaction,
                   member:discord.Member,
                   channel:discord.VoiceChannel):
        

        perms=channel.permissions_for(interaction.user)
        if perms.connect :
            old=member.voice.channel
            await member.move_to(channel)
            embed=discord.Embed(
                colour=discord.Colour.from_rgb(9, 13, 138)
            )
            mover=interaction.user.name
            
            embed.add_field(
                name="Member Moved",
                value=(f"`{mover}` moved `{member}` form **{old}** to **{channel.name}**"))
            await interaction.response.send_message(embed=embed)
        elif not(perms.connect):
            await interaction.response.send_message("**You do not have permission to view or connect to that voice channel.**",ephemeral=True)



async def setup(bot):
    await bot.add_cog(move_command(bot))



