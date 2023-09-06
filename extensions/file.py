import discord
from discord.ext import commands
from client.bot import Bot

class File(commands.Cog):
    def __init__(self, bot : Bot) -> None:
        super().__init__()
        self.bot = bot
    @commands.command(name='file')
    async def get(self, ctx : commands.Context ,line : int):
        # Checker For User
        await ctx.send("Send The File")
        def checker(message : discord.Message):
            return message.author == ctx.author and message.attachments
        file_msg = await self.bot.wait_for('message', check=checker)
        file = file_msg.attachments[0]
        print(file.content_type)
        if not file.filename.endswith('.txt'):
            await ctx.send("The Format of File Must be txt")
        else:
            file_content = await file.read()
            entry_line = file_content.decode().split('\n')
            await ctx.send(entry_line[line - 1])

async def setup(bot : Bot):
    await bot.add_cog(File(bot))