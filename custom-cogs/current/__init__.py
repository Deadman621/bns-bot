from .current import CurrentCog

async def setup(bot):
    await bot.add_cog(CurrentCog(bot))

