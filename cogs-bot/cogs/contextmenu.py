import discord
from discord import app_commands
from discord.ext import commands

@app_commands.context_menu(name="Click")
async def click(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f"You clicked on {user.mention}")

class ContextMenuCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.tree.add_command(click)

async def setup(bot):
    await bot.add_cog(ContextMenuCog(bot))