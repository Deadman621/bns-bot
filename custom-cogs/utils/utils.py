import discord
from redbot.core import commands, app_commands

class UtilsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Get equivalent nether coordinates.")
    @app_commands.describe(x="X Coordinate", y="Y Coordinate", z="Z Coordinate")
    async def coords(self, interaction: discord.Interaction, x: float, y: float, z: float):
        Xn = x / 8
        Yn = y / 8
        Zn = z / 8
        embed = discord.Embed(
            title='Equivalent Nether Coordinates',
            description=f'**Given Overworld Coordinates:**\n```py\nX = {x}, Y = {y}, Z = {z}```\n**Equivalent Nether Coordinates:**\n```py\nX = {Xn}, Y = {Yn}, Z = {Zn}```',
            colour=9391345,
        )
        embed.set_author(name='BABU Nova Squadron (BNS)', icon_url='https://media.discordapp.net/attachments/1119010722979004456/1121162670247252028/BNS_Logo.png?width=473&height=473')
        await interaction.response.send_message(embed=embed, ephemeral=False)

