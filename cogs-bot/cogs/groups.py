import discord
from discord import app_commands
from discord.ext import commands

class CommandGroup(app_commands.Group):
    def __init__(self, bot):
        super().__init__(
            name="group"
        )
        
        self.bot = bot

    @app_commands.command(name="one", description="The first command of the group")
    async def removeblacklist(self, interaction: discord.Interaction):
        await interaction.response.send("One!") 

    @app_commands.command(name="two", description="The second command of the group")
    async def removeblacklist(self, interaction: discord.Interaction):
        await interaction.response.send("Two!")
    
    @app_commands.command(name="three", description="The third command of the group")
    async def removeblacklist(self, interaction: discord.Interaction):
        await interaction.response.send("Three!")

class CommandGroupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.group = CommandGroup(bot=self.bot)

        self.bot.tree.add_command(self.group)

    def cog_unload(self):
        self.bot.tree.remove_command(self.group.name, type=discord.AppCommandType.message)


async def setup(bot):
    await bot.add_cog(CommandGroupCog(bot))