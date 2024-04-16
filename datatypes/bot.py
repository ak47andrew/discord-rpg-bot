import discord
from discord.ext import commands
import os
from datatypes import coloriser


class Bot(commands.Bot):
    def __init__(self, token: str):
        super().__init__(command_prefix="/", intents=discord.Intents.all())
        self.token = token

    async def setup_hook(self) -> None:
        for cog in os.listdir("cogs"):
            try:
                await self.load_extension(cog)
                coloriser.green(f"Successfully loaded cog \"{cog}\"")
            except Exception as e:
                coloriser.red(f"Failed to load cog \"{cog}\": {e}")

    async def on_ready(self):
        coloriser.blue("Ready!")

    def run(self) -> None:
        super().run(self.token)
