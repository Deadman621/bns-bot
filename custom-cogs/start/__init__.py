from .start import StartCog

async def setup(bot):
    await bot.add_cog(StartCog(bot))