import discord
from discord.ext import commands
from client.bot import Bot

class Log(commands.Cog):
    def __init__(self, bot : Bot) -> None:
        super().__init__()
        self.bot =bot
    @commands.Cog.listener()
    async def on_message_edit(self, before : discord.AuditLogEntry.before, after : discord.AuditLogEntry.after):
        channel = before.channel
        log_channel = self.bot.get_channel(1056990464798117938)
        await log_channel.send(f'Edited {before.content} -> {after.content}')

async def setup(bot : Bot):
    await bot.add_cog(Log(bot))