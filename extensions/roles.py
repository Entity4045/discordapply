import discord
from discord.ext import commands
from client.bot import Bot

class Menu(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Green', emoji="🟢", description="Green Role"),
            discord.SelectOption(label='Black', emoji="⚫", description = "Black Role"),
            discord.SelectOption(label='Blue', emoji="🔵", description = "Blue Role")
        ]
        super().__init__(placeholder="Select a Color",max_values=1,min_values=1,options=options)
    async def callback(self, interaction : discord.Interaction):
        if self.values[0] == "Green":
            role = interaction.guild.get_role(1148945342671376464)
            members_role = role.members
            if interaction.user in members_role:
                await interaction.user.remove_roles(role)
                await interaction.response.send_message(f"{interaction.user.mention} Removed {role.mention}")
            else:
                await interaction.user.add_roles(role)
                await interaction.response.send_message(f"{interaction.user.mention} Done {role.mention}")
        elif self.values[0] == "Black":
            role = interaction.guild.get_role(1148945370416693268)
            members_role = role.members
            if interaction.user in members_role:
                await interaction.user.remove_roles(role)
                await interaction.response.send_message(f"{interaction.user.mention} Removed {role.mention}")
            else:
                await interaction.user.add_roles(role)
                await interaction.response.send_message(f"{interaction.user.mention} Done {role.mention}")
        elif self.values[0] == "Blue":
            role = interaction.guild.get_role(1148945403421655060)
            members_role = role.members
            if interaction.user in members_role:
                await interaction.user.remove_roles(role)
                await interaction.response.send_message(f"{interaction.user.mention} Removed {role.mention}")
            else:
                await interaction.user.add_roles(role)
                await interaction.response.send_message(f"{interaction.user.mention} Done {role.mention}")

class MenuView(discord.ui.View):
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)
        self.add_item(Menu())

class Roles(commands.Cog):
    def __init__(self, bot : Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name='roles')
    async def roles(self, ctx : commands.Context):
        await ctx.send("Choose The items", view=MenuView())

async def setup(bot : Bot):
    await bot.add_cog(Roles(bot))