import discord
import asyncio
import logging
import os
from discord.ext import commands
from client.bot import Bot

# --------- Logger --------

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
log_file_path = os.path.join('logs', 'discord.log')
handler = logging.FileHandler(filename=log_file_path, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# --------- End Logger --------

# --------- Define The Bot --------

intents = discord.Intents.all()
bot = Bot(command_prefix="I!",intents=intents,allowed_mentions = discord.AllowedMentions(everyone=False, roles=False))
bot.remove_command('help')

# --------- End Define The Bot --------

# --------- Advanced Run --------

async def run():
    async with bot:
        await bot.start("MTA2NjQxMTA5NjA0NDQ3NDM5OA.GX0Tr9.v6g5IrbC_nG-XHCEyZMlCMzW0S7_xIfZrBlpIw")

asyncio.run(run())

# --------- End Advanced Run --------