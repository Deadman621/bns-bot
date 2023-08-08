from .utils import UtilsCog

async def setup(bot):
    await bot.add_cog(UtilsCog(bot))