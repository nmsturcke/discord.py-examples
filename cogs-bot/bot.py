import os
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
    
    async def on_ready(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    await bot.load_extension(f"cogs.{filename[:-3]}")
                    print(f"Loaded {filename}")
                except Exception as e:
                    print(f"Failed to load {filename}")
                    print(f"[ERROR] {e}")

        await self.tree.sync()
        print("Successfully synced commands")
        print(f"Logged onto {self.user}")

bot = Bot()
bot.run('token')