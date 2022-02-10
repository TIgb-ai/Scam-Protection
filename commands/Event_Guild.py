from ast import Not
import nextcord
from nextcord import *
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from psutil import NIC_DUPLEX_UNKNOWN
import pymongo
from nextcord.abc import GuildChannel
from datetime import datetime


mongodbai = pymongo.MongoClient('mongodb+srv://mira:immune@mira.bqrza.mongodb.net/mira?retryWrites=true&w=majority')
dbclient = mongodbai['scam']
log_collection = dbclient['logs_chan']
whitelisted = dbclient['whitelisted']
not_found = "Not Set"
embed_colour = 0x36393F
blacklisted_user = dbclient['blacklisted_user']


class Event_Guild(commands.Cog):
    '''Guild Join Event Here'''
    
    
    def __init__(self, bot):
        self.bot=bot
        
    @commands.Cog.listener()
    async def on_member_join(self,member):
        already_t = blacklisted_user.find_one({'_id': int(member.id)})
        if already_t is None:
            pass
        if already_t is not None:
            chan = log_collection.find({'_id': int(member.guild.id)})
            chan_info =  chan[0]["channel_id"]
            logs = self.bot.get_channel(chan_info)
            em = nextcord.Embed(title = f"⚠Alert !! Suspecious User⚠")
            em.description=f"\n\n**Suspecious User Joined** = {member.mention}"
            em.color = embed_colour
            em.add_field(name="Suspect",value=f"{member.mention}")
            em.add_field(name="User is Blacklisted",value=f"`Seems user is suspecious of being already hacked!!`")
            em.add_field(name="Need For Action?",value=f"`Probably yes!!`")
            em.timestamp= datetime.now()
            await logs.send(embed=em)
            
            
            
        
        
        
        
        
        
        
        
        
        
        


def setup(bot):
    bot.add_cog(Event_Guild(bot))
    print('Guild Events - ✔')