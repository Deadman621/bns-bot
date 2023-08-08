import discord
from discord.ext.commands import has_any_role
from redbot.core import commands, app_commands, checks

class ModpackCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.modpack_info = None
 
    modify = app_commands.Group(name="modify", description="Modify /modpack command")
 
    @modify.command(name="add", description="Add modpack & relating information to /modpack")
    @app_commands.describe(modpack="Add modpack", download_link="Download link of the modpack", showcase_video="Showcase Video:")
    async def modify_add(self, interaction: discord.Interaction, modpack: str, download_link: str, showcase_video: str):
        self.modpack_info = {
            "modpack": modpack,
            "download_link": download_link,
            "showcase_video": showcase_video
        }
        await interaction.response.send_message(f"Modpack changed to {modpack}, Download Link: {download_link}, Showcase Video: {showcase_video}.", ephemeral=False)

    @modify.command(name="null", description="Reverts /modpack to no modpack running.")
    async def modify_null(self, interaction: discord.Interaction):
        self.modpack_info = None
        await interaction.response.send_message("/modpack set to null value. No modpacks are currently running on the server.", ephemeral=False)
     
    @app_commands.command(description="Shows which modpack is currently running.")
    async def modpack(self, interaction: discord.Interaction):
        if self.modpack_info is None:
            await interaction.response.send_message("No modpack is being played currently.", ephemeral=True)
        else:
            modpack = self.modpack_info["modpack"]
            download_link = self.modpack_info["download_link"]
            showcase_video = self.modpack_info["showcase_video"]

            embed = discord.Embed(
                title='MODPACK',
                description=f"The current Modpack being played is {modpack}. Please see https://discord.com/channels/1110317424290578505/1119010267045560431 for more information.\n\n[Download Link]({download_link}) • [Showcase Video]({showcase_video})\n\n**Server IP:** ```bns.modpack.falix.gg```\n\nLiking {modpack}? Don't forget to upvote, if enough upvotes, {modpack} will be played for another week!",
                colour=9391345,
            )

            embed.set_image(url='https://cdn.discordapp.com/attachments/1119010722979004456/1121879560217178215/BNS_Banners_1.png')
            embed.set_author(name='BABU Nova Squadron (BNS)', icon_url='https://media.discordapp.net/attachments/1119010722979004456/1121162670247252028/BNS_Logo.png?width=473&height=473')
            embed.set_footer()
            await interaction.response.send_message(embed=embed, ephemeral=False)