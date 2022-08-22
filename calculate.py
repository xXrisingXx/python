from cProfile import label
from faulthandler import disable
import os
import discord
#from discord.ui import Select, View
from discord import Embed
from discord import app_commands, Interaction
from discord.ext import commands
import random
import dotenv


# Read the PNG Image in BGR format

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

PREFIX = os.getenv('PREFIX')
class val:
    number = ''     # Class Variable
    def __init__(self, name):
        self.name = name
#---------------------------------------------------
class calculator(commands.Cog):
    value = ""
    def __init__(self, bot):
        self.bot = bot
    
    #This is a hybrid command it works as a slash command "/calculate (number)"" and a text command "";calculate (number).""
    @commands.hybrid_command(name='calculate', with_app_command=True, describe="Calculates how many coins it cost for so many potions.")
    async def calculate(self, ctx, num):
        #Calculate description for the ui.
        "Calculates how many coins it cost for so many potions."
        if str(num).isnumeric() == True: #This checks if someone uses numbers only, if they dont then it's false and will send a reponse.
            calculator.value = num
            if int(num) == 1:
                embeded =  discord.Embed(description="Calculated <"+num+"> potion.", color=ctx.author.color)
                await ctx.send(embed=embeded, view=MyView())
                number = val(int(num))
                return number
            elif int(num) > 1:
                embeded =  discord.Embed(description="Calculated <"+num+"> potions.", color=ctx.author.color)
                await ctx.send(embed=embeded, view=MyView())
                number = val(int(num))
                return number
        elif str(num).isnumeric() == False:
            #These are the responses it's going to send.
            quotes = [
                "I can't calculate letters you idiot.",
                "Letters are not aloud. Try again with a number idiot.",
            ]
            response = random.choice(quotes)
            await ctx.send("```\n"+response+"```")
    
    #This sends the source code link on my github.
    @commands.hybrid_command()
    async def source(self, ctx):
        "Sends the source code to this script."
        #This embeds the message so you can click the link. If not embeded you link will just send as a text and not a link.
        embeded = discord.Embed(title="Source", description="The source code to my calculate function is located at this link (https://github.com/xXrisingXx/python/blob/main/calculate.py).", color=ctx.author.color)
        await ctx.send(embed=embeded)

class MyView(discord.ui.View):
    @discord.ui.select(
        placeholder="Choose a potion to calculate.⬇️",
        disabled=False,
        options=[
            discord.SelectOption(
                label="Super Glue",
                emoji="🧪",
                description="1 Super Glue cost 65.3 coins.",
            ),
            discord.SelectOption(
                label="Superior Portal Gun",
                emoji="🌀",
                description="1 Superior Portal Gun cost 84 coins.",
            ),
        ]
    )

    async def select_callback(self, interaction, select): #The function called when the user is done selecting options
        val0 = calculator.value
        if select.values[0] == "Super Glue":
            #format will format the text to have a comma for instance (3000000) will be (3,000,000). int(val0) turns value into a integer type. It was a string a before
            val1,val2="{:,}".format(int(val0)),65.34
            #This rounds down to the nearest whole number and formats it as well.
            num="{:,}".format(round(float(val0) * val2))
            await interaction.response.send_message("```\n("+str(val1)+") glues roughly cost ("+str(num)+")\n```")
            #---------------------------------------------------
            select.disabled=True
            select.placeholder="Selection has ended."
            await interaction.message.edit(view=self)
        elif select.values[0] == "Superior Portal Gun":
            #format will format the text to have a comma for instance (3000000) will be (3,000,000). int(val0) turns value into a integer type. It was a string a before
            val1,val2="{:,}".format(int(val0)),84
            #This rounds down to the nearest whole number and formats it as well.
            num="{:,}".format(round(float(val0) * val2))
            await interaction.response.send_message("```\n("+str(val1)+") portals roughly cost ("+str(num)+")\n```")
            #---------------------------------------------------
            select.disabled=True
            select.placeholder="Selection has ended."
            await interaction.message.edit(view=self)

    async def interaction_check(self, interaction: Interaction) -> bool:
        return await super().interaction_check(interaction)

async def setup(bot):
    await bot.add_cog(calculator(bot))
