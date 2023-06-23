from .modpack import ModpackCog

async def setup(bot):
    await bot.add_cog(ModpackCog(bot))

