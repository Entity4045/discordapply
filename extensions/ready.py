import discord
from discord.ext import commands
from client.bot import Bot

class Ready(commands.Cog):
    def __init__(self, bot : Bot):
        # Define The Bot in the Class
        self.bot = bot
    # Ready Event
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user.name}")

async def setup(bot : Bot):
    await bot.add_cog(Ready(bot))