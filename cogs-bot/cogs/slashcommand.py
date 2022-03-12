import discord
from discord import app_commands
from discord.ext import commands

class FirstCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="cog", description="This command comes from a cog!")
    async def fromcog(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello, I'm sending from the cog!")

def setup(bot):
    bot.add_cog(FirstCog(bot))