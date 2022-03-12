import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
    
    async def on_ready(self):
        await self.tree.sync()

@app_commands(name="first", description="The first command!")
async def first(self, interaction: discord.Interaction):
    await interaction.response.send_message(content="Hello!")

bot = Bot()
bot.run('token')