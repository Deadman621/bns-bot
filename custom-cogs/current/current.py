import discord
from redbot.core import commands, app_commands

class CurrentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.describe(modpack="Add modpack", download_link="Download link of the modpack", showcase_video="Showcase Video:")
    @commands.has_any_role("Admin", "Moderator")
    async def modify(self, interaction: discord.Interaction, modpack: str, download_link: str, showcase_video: str):
        await interaction.response.send_message(f"Modpack changed to {modpack}, Download Link: {download_link}, Showcase Video: {showcase_video}.", ephemeral=False)
        global mdpk
        mdpk = modpack
        global down
        down = download_link
        global show
        show = showcase_video

    @app_commands.command()
    async def current(self, interaction: discord.Interaction):
        try:    
            embed = discord.Embed(
                title='MODPACK',
                description=f'The modpack currently played is **{mdpk}**. Please see https://discord.com/channels/1110317424290578505/1119010267045560431 for more information.\n\nDownload Link: {down}\nShowcase Video: {show}\n\nServer IP: 123',
                colour=9391345,
            )

            embed.set_image(url='https://cdn.discordapp.com/attachments/1119011931643203606/1121172590061428968/BNS_Banners.png')
            embed.set_author(name='BABU Nova Squadron (BNS)', icon_url='https://media.discordapp.net/attachments/1119010722979004456/1121162670247252028/BNS_Logo.png?width=473&height=473')

            
            await interaction.response.send_message(embed=embed, ephemeral=False)
        except NameError:
            await interaction.response.send_message("No Modpack is being played currently", ephemeral=True)
