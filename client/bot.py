import discord
from discord.ext import commands
from typing import Any

# ---- Extensions ----

extensions = (
    'extensions.ready',
    'extensions.roles',
    'extensions.file',
    'extensions.log'
)

# ---- Extensions ----

# ---- Subclassing commands.Bot ----

class Bot(commands.Bot):
    def __init__(self, *args : Any, **kwargs : Any) -> None:
        super().__init__(*args, **kwargs)
    async def setup_hook(self) -> None:
        # Load Extensions
        for i in extensions:
            await self.load_extension(i)
            print(f"We Loaded {i}")
        # Load Slash commands
        await self.tree.sync()
# ---- Subclassing commands.Bot ----