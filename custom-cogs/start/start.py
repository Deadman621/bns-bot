import discord
from redbot.core import commands, app_commands

class StartCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Get information on how to start the server.")
    async def start(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title='Starting Server',
            description="As you may know that the server currently is not 24/7, if you'd like to play anytime you can start the server by following the instructions below.\n\n- Visit the [URL](https://falixnodes.net/start).\n- input the Server IP.\n- Wait for verification.\n- Click Submit.\n\n**Server IPs:**```\nModpack: game1.falixserver.net:24480\nSurvival: game7.falixserver.net:10065```\n*If the above mentioned steps do not work, try using incognito mode and retry. Also Make sure the server is offline before trying to start it. The user status (i.e Online or Offline) of <@1126524011728343090> and <@1126629384418242591> will indicate if the server is Online or Offline.*",
            colour=9391345,
        )                                                 

        embed.set_author(name='BABU Nova Squadron (BNS)', icon_url='https://media.discordapp.net/attachments/1119010722979004456/1121162670247252028/BNS_Logo.png?width=473&height=473')
        await interaction.response.send_message(embed=embed, ephemeral=False)

    @app_commands.command(description="Get information on how to extend the server timer.")
    async def timer(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title='Extending Timer',
            description="Server will shutdown after an hour if the time is not extended. When the server is about to shutdown a message will be displayed in chat 20 or so minutes prior indicating to add time. Follow the steps below to add time.\n\n- Go to the Add Time URL for the server.\n - For Modpack Server [Visit](https://client.falixnodes.net/timer?id=1017968).\n - For Survival Server [Visit](https://client.falixnodes.net/timer?id=1020655).\n- Wait for human verification.\n- Click **Add +1 Hour.**\n\n*Due to restrictions from the hosts, you can only add 3 hours of time at the same point, you have to wait till the timer is below 3 hours to add more time. Other than that there are no restrictions if the server will be shut down given that the timer is being constantly added by a user.*",
            colour=9391345,
        )

        embed.set_author(name='BABU Nova Squadron (BNS)', icon_url='https://media.discordapp.net/attachments/1119010722979004456/1121162670247252028/BNS_Logo.png?width=473&height=473')
        await interaction.response.send_message(embed=embed, ephemeral=False)