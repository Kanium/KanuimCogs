import discord
import json
import requests
from redbot.core import Config, checks, commands

embed = requests.get("https://raw.githubusercontent.com/Kanium/KanuimCogs/master/welcomeCog/embedded_message.json").text

def fetchMessage(jsonFormat):
    try:
        message=discord.Embed(title=str(jsonFormat['title']), description=''.join(map(str, jsonFormat['description'])), color=hex(jsonFormat['color']))      
        message.set_thumbnail(url=jsonFormat['thumbnail'])
        for field in jsonFormat['fields']:
            if(field['id']!='links'):
                message.add_field(name=field['name'], value=field['value'], inline=field['inline'])
            else:
                message.add_field(name=field['name'], value=''.join(map(str,field['value'])), inline=field['inline'])

        message.set_footer(text=jsonFormat['footer']['text'], icon_url=jsonFormat['footer']['icon_url'])
        return message

    except:
        return 'Welcome To Kanuim !'

class WelcomeCog():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = json.loads(str(embed))

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        try:
            message = fetchMessage(self.message)
            await member.send(content=None, embed=message)
        except:
            print(
                f'Error Occured! sending a dm to {member.display_name} didnt work !')
