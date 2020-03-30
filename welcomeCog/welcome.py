import asyncio
import discord
import json

from redbot.core import Config, checks, commands
from redbot.core.utils.chat_formatting import box, humanize_list, pagify

jsonFile = '''\
{\
    "title":"Welcome to the Kanium Discord!",\
    "description":[\
        "\n",\
        "Please ensure to have a look at our #public_info channel and understand who we are and how this place works.",\
        "\n\n",\
        "Additionally it must be mentioned that being on our Discord and playing games with us, does not require Kanium membership. We,",\
        "on the other hand, expect that those who seek to apply for membership show earnestness- in both application and in becoming part of the community"\
    ],\
    "color":"0x3399ff",\
    "thumbnail": "https://i.imgur.com/4TLdfDA.png",\
    "fields":[\
        {"id":"text", "name":"Apply to join Kanuim", "value":"!apply applicationText", "inline":"True"},\
        {"id":"text", "name":"Description", "value":"Use this to submit an application for joining Kanium", "inline":"True"},\
        {"id":"text", "name":"Enjoy your stay", "value":"Feel free to hang out in the chat rooms. If you're looking to play a specific game, join that game's chat channel", "inline":"False"},\
        {"id":"links", "name":"Useful information", "value":[ \
            "\n",\
            "[KANIUM Website](https://www.kanium.org/)",\
            "\n",
            "[KANIUM Steam Group](https://steamcommunity.com/groups/Kanium)",\
            "\n",
            "[KANIUM Twitch Channel](https://twitch.tv/kaniumtv)",\
            "\n",
            "[KANIUM Open Collective](https://opencollective.com/kanium)"\
        ], "inline":"True"},
        {"id":"text", "name":"Apply to join Kanuim", "value":"!apply applicationText", "inline":"True"}\
    ],\
    "footer":{\
        "text":"If you have any questions, please ping a @Recruiter",\
        "icon_url":"https://i.imgur.com/4TLdfDA.png"\
    }\
}\
'''

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
        message=discord.Embed(title="Kanuim", description='', color=hex(jsonFormat['color']))     
        message.add_field(name="Welcome", value='Welcome To Kanuim !', inline=True) 
        return message

class WelcomeCog(commands.Cog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = json.loads(jsonFile)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        try:
            message = fetchMessage(self.message)
            await member.send(content=None, embed=message)
        except (discord.NotFound, discord.Forbidden):
            print(f'Error Occured! sending a dm to {member.display_name} didnt work !')
