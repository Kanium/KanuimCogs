import discord

from datetime import datetime, timedelta
from redbot.core import Config, commands
from threading import Timer



class EventsCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=hash(datetime.now())) #crude and will totally not cause issues todo add unique id

        #todo more config for redbot nessesary since we will list events ....
        self.title = ""
        self.date_time = None
        self.message_list=[]

    def generate_body(self):
        return "msg body to display on discort" #todo

    @commands.command(pass_context=True)
    async def event(self,ctx, *args): #anyone in the guild
        try:
            self.title = args[0]
            self.date_time = datetime.strptime(args[1]+' '+args[2], '%d/%m/%y %H:%M') #yeah time is an issue this is temporary
            t = Timer((datetime.now()-self.date_time.replace(minute=self.date_time.minute-15)).total_seconds(), self.send_reminder)
            msg = await ctx.send("message")
            self.message_list.append({'id':msg.id,'attendance': [ctx.author.id]})
        except:
            await ctx.send('Not a valid argument! event is !event [title] [date] [time] without seconds')

    @commands.command()
    async def seteventchannel(self): #admin only

    @commands.Cog.listener()
    async def on_reaction_remove(self,reaction, user) -> None:
        #substitute user for the actuall user id. 
        for data in self.message_list:
            if reaction.message.id in data["id"] and "user" in data["attendance"]:
                data["attendance"].remove("user")





    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user) -> None:
        for data in self.message_list:
            if reaction.message.id in data["id"]:
                #get reaciton emoji
                data["attendance"].append("user")



    async def send_reminder(self,ctx):
        for user in self.registered_users["Reminder"]:
            ctx.send(f"")
