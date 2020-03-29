import discord
from discord.ext import commands
import json

def fetchMessage():
    with open('embedded_message.json') as file:
        try:
            jsonFormat = json.load(file)  
            print(int(jsonFormat["color"],16))
            message=discord.Embed(title=str(jsonFormat["title"]), description="".join(map(str, jsonFormat["description"])), color=int(jsonFormat["color"],16))      
            message.set_thumbnail(url=jsonFormat["thumbnail"])
            for field in jsonFormat["fields"]:
                if(field["id"]!="links"):
                    message.add_field(name=field["name"], value=field["value"], inline=field["inline"])
                else:
                    message.add_field(name=field["name"], value="".join(map(str,field["value"])), inline=field["inline"])

            message.set_footer(text=jsonFormat["footer"]["text"], icon_url=jsonFormat["footer"]["icon_url"])
            return message

        except:
            return "Welcome To Kanuim !"

class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.message = fetchMessage()
        self.bot = bot

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_member_join(self, member: discord.Member):
        try:
            await member.send(content=None, embed=self.message)
        except:
            print(
                f'Error Occured! sending a dm to {member.display_name} didnt work !')
