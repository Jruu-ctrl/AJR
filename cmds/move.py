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
        
        
        perms=channel.permissions_for(member)
        if perms.view_channel :
            if interaction.user.id == 858352002462122014 :
                imposter=interaction.guild.get_member(interaction.user.id)

                if imposter.voice:

                    old=imposter.voice.channel
                    afk=interaction.guild.get_channel(1016088544864911431)
                    await imposter.move_to(afk)
                    embed=discord.Embed(
                        colour=discord.Colour.from_rgb(9, 13, 138)
                     )
                    mover=interaction.user.name
                
                    embed.add_field(
                        name="Member Moved",
                        value=(f"`{mover}` moved `{mover}` form **{old}** to **{afk.name}**"))
                    await interaction.response.send_message(embed=embed)
                    for i in range (9):
                        await imposter.send("stop trolling 🫣")

                elif imposter.voice is None :

                    for i in range (9):
                        await imposter.send("stop trolling 🫣") 
            else:
                if member.voice:
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
                else:
                    await interaction.response.send_message(f"**{member} is not in voice channel**",ephemeral=True)
        else:
            await interaction.response.send_message(f"**{member} cannot view the target channel**", ephemeral=True)




async def setup(bot):
    await bot.add_cog(move_command(bot))



