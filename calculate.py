import os
import discord
from discord.ui import Select, View
from discord import Embed
from discord import interactions
from discord import app_commands
from discord.ext import commands
import random
import dotenv


# Read the PNG Image in BGR format

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

POTION = os.getenv('POTION')
AMOUNT = os.getenv('ACCOUNTS')
PAUSE = os.getenv("PAUSE")
#---------------------------------------------------
class calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='calculate', with_app_command=True, describe="Calculates how many coins it cost for potions.")
    async def calculate(self, ctx, num):
        #potion description
        "Calculates how many coins it cost for potions."
        if str(num).isnumeric() == True:
            selection = Select(
                placeholder="Choose a potion to calculate.⬇️",
                options=[
                discord.SelectOption(
                    label="Super Glue",
                    emoji="🧪",
                    description="1 Super Glue cost 65.3 coins."),
                discord.SelectOption(
                    label="Superior Portal Gun",
                    emoji="🌀",
                    description="1 Superior Portal Gun cost 84 coins."),
            ])

            view = View()
            view.add_item(selection)
            view.message = await ctx.send(view = view)
            async def my_callback(interaction):
                val0=num
                if selection.values[0] == "Super Glue":
                    val1,val2="{:,}".format(int(val0)),65.34
                    num="{:,}".format(round(float(val0) * val2))
                    await ctx.send("```\n("+str(val1)+") glues roughly cost ("+str(num)+")\n```")
                elif selection.values[0] == "Superior Portal Gun":
                    val1,val2="{:,}".format(int(val0)),84
                    num="{:,}".format(round(float(val0) * val2))
                    await ctx.send("```\n("+str(val1)+") portals roughly cost ("+str(num)+")\n```")

            selection.callback = my_callback 
            
        elif str(num).isnumeric() == False:
            quotes = [
                "I can't calculate letters idiot.",
                "Letters are not aloud. Try again with a number idiot.",
            ]
            response = random.choice(quotes)
            await ctx.send("```\n"+response+"```")

    @commands.hybrid_command()
    async def source(self, ctx):
        embed = Embed
        embed.description = "Here is my source code to this command (your_link_goes_here)."
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(calculator(bot))
