from discord.ext import commands
import discord

class CurrentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        if not hasattr(self.bot, "slash"):
            self.bot.slash = commands.SlashCommand(self.bot, override_type=True)
            await self.bot.slash.sync_all_commands()

    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, error):
        await ctx.send(f"An error occurred: {str(error)}")

    @commands.Cog.listener()
    async def on_slash_command(self, ctx):
        if ctx.name == "current":
            embed = discord.Embed(
                title="Current Status",
                description="This is the current status.",
                color=discord.Color.blue()
            )
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(CurrentCog(bot))
