import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
    
    async def on_ready(self):
        await self.tree.sync()
        print("Successfully synced commands")
        print(f"Logged onto {self.user}")

bot = Bot()

@bot.tree.command(name="first", description="The first command!")
async def first(interaction: discord.Interaction):
    await interaction.response.send_message(content="Hello!")

bot.run('token')
