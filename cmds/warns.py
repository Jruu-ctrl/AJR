from discord.ext import commands
from discord import app_commands
import discord
from datetime import timedelta

class warn_commands(commands.Cog):
    def __init__(self,bot):
        self.bot=bot


    @app_commands.command(name="warn", description="Warn a user for rule violations. The warning is logged for moderation purposes.")
    @app_commands.describe(
        user="The user to warn",
        reason="Reason for the warning"
        )
    async def warn(self,
                   interaction:discord.Interaction,
                   user:discord.Member,
                   reason:str =""):
        
        if not interaction.user.guild_permissions.kick_members:
            await interaction.response.send_message("You do not have the `kick_members` permissions to use this command.")
            return
        
        admin=interaction.user.name

        embed=discord.Embed(
            colour=discord.Colour.from_rgb(9, 13, 138)
            )

        if reason != "":
             
             embed.add_field(name="Warn Details",
                             value=(f"Admin: `{admin}`\nWarned user: `{user}`"
                             f"\nUser ID: ||{user.id}||"
                             f"\nReason: {reason}"))
             embed.set_thumbnail(url=user.display_avatar.url)
             await user.send(embed=embed)

        else:

            embed.add_field(name="Warn Details",
                            value=(f"Admin: `{admin}`"
                            f"\nWarned user: `{user}`"
                            f"\nUser ID: ||{user.id}||"))
            
            embed.set_thumbnail(url=user.display_avatar.url)
await user.send(embed=embed)

        await interaction.response.send_message(embed=embed)


    @app_commands.command(name="ban_forum", description="Ban a user for rule violations. The ban is logged for moderation purposes.")
    @app_commands.describe(
        user="The user to ban",
        duration="The duration of the ban (e.g., 7d or permanent)",
        reason="The reason for the ban",
        reported_by="The user who reported this member"
    )
    async def ban(self,
                   interaction:discord.Interaction,
                   user:discord.Member,
                   duration:str,
                   reason:str,
                   reported_by:discord.Member
                   ):
        
        if not interaction.user.guild_permissions.kick_members:
            await interaction.response.send_message("You do not have the `kick_members` permissions to use this command.")
            return
        
        if not interaction.guild.me.guild_permissions.moderate_members:
            await interaction.response.send_message("I do not have the `MODERATE_MEMBERS` permissions to mute this user.", ephemeral=True)
            return
        
        admin=interaction.user.name

        embed=discord.Embed(
            colour=discord.Colour.from_rgb(9, 13, 138)
            )

        embed.add_field(name="Ban Details",
                        value=(
                        f"Admin: `{admin}`"
                        f"\nWarned user: `{user}`"
                        f"\nUserID: ||{user.id}|| "
                        f"\nDuration: {duration} "
                        f"\nReason: {reason}"
                        f"\nReported by:`{reported_by.name}`"))
        
        embed.set_thumbnail(url=user.display_avatar.url)

        unit=duration[-1].lower()

        dur=int(duration[:-1])

        if unit=="s":
            time=timedelta(seconds=dur)
        elif unit=="m":
            time=timedelta(minutes=dur)
        elif unit=="h":
            time=timedelta(hours=dur)
        elif unit=="d":
            time=timedelta(days=dur)
        else:
            await interaction.response.send_message("Please choose a valid unit of time (e.g., `s`, `m`, `h`, or `d`).",ephemeral=True)
            return
        
        await interaction.response.send_message(embed=embed)

        await user.send(embed=embed)

        try:
            await user.timeout(time, reason=f"Muted for {dur} {unit}")
        except discord.Forbidden:
            await interaction.followup.send("I don't have the required permissions to timeout this user.", ephemeral=True)
            return


async def setup(bot):
    await bot.add_cog(warn_commands(bot))



