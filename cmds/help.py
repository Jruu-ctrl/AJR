from discord.ext import commands
from discord import app_commands
import discord

class help_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @app_commands.command(name="help", description="Displays a list of available commands and their descriptions.")
    async def slash_help(self, interaction: discord.Interaction):
        embed = self.build_help_embed()
        await interaction.response.send_message(embed=embed, ephemeral=True)

    
    @commands.command(name="help", description="Displays a list of available commands and their descriptions.")
    async def prefix_help(self, ctx: commands.Context):
        embed = self.build_help_embed()
        await ctx.send(embed=embed)

    
    def build_help_embed(self):
        embed = discord.Embed(
            title="Bot Commands",
            description="Here’s a list of available commands:",
            color=discord.Color.from_rgb(9, 13, 138)
        )
        
        embed.add_field(
            name=":warning: `/warn`",
            value="Warn a user for rule violations. Requires `kick_members` permission.",
            inline=False
        )

        embed.add_field(
            name=":no_entry_sign: `/timeout`",
            value="Timeout (mute) a user for a set duration. Requires `kick_members` permission.",
            inline=False
        )

        embed.add_field(
            name=":twisted_rightwards_arrows: `/move`",
            value="Move a member to another voice channel if they can view it.",
            inline=False
        )

        embed.set_footer(text="More features coming soon!")
        return embed

async def setup(bot):
    await bot.add_cog(help_commands(bot))
