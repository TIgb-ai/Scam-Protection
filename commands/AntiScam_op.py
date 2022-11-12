import nextcord ,pymongo
from nextcord import *
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from nextcord.abc import GuildChannel
from datetime import datetime
from nextcord.ext.commands import has_permissions, MissingPermissions
#####################################################################################################################################################
##################################################################################################################################################### 
mongodbai = pymongo.MongoClient('database_link')
dbclient = mongodbai['scam']
log_collection = dbclient['logs_chan']
mention_prot = dbclient['mention_prot_state']
blacklisted_user = dbclient['blacklisted_user']
whitelisted = dbclient['whitelisted']
embed_colour = 0x36393F
#####################################################################################################################################################
##################################################################################################################################################### 
whitelisted_words = [
    "discord.gg","discord.gg/","discord.gift/","discord.gift","cdn.discordapp.com",
    "discord.media","images-ext-1.discordapp.net","images-ext-2.discordapp.net","images-ext-3.discordapp.net"
    ]

blacklist = [
    "@everyone"
]
#####################################################################################################################################################
##################################################################################################################################################### 
class optfeature(commands.Cog):
    '''optfeature Command'''
    
    
    def __init__(self, bot):
        self.bot=bot
        
        
    @commands.Cog.listener()
    async def on_message(self,message):
        if isinstance(message.channel, nextcord.channel.DMChannel) and message.author != self.bot.user:
            pass
        chan_f = log_collection.find_one({'_id': int(message.guild.id)})
        mention_f = mention_prot.find_one({'_id': int(message.guild.id)})
        role_f = whitelisted.find_one({'_id': int(message.guild.id)})
        if chan_f is None:
            pass
        elif mention_f is None:
            pass
        if message.author is nextcord.Member.bot:
            return
        if message.author.guild_permissions.manage_messages:
            return
        if message.author.guild_permissions.administrator:
            return
        if role_f is None:
            pass

        if chan_f and mention_f is not None:
            chan = log_collection.find({'_id': int(message.guild.id)})
            # mention = mention_prot.find_one({'_id': int(message.guild.id)})
            chan_info =  chan[0]["channel_id"]
            # mention_info = mention[0]["_id"]
            if any(word in message.content for word in whitelisted_words):
                pass
                
            elif any(word in message.content for word in blacklist):
                if any(word in message.content for word in whitelisted_words):
                    pass
                else:
                    await message.delete()
                    already_t = blacklisted_user.find_one({'_id': int(message.author.id)})
                    if already_t is not None:
                        logs = self.bot.get_channel(chan_info)
                        em = nextcord.Embed(title = f"<a:robber:933369380581036062> User Caught <a:robber:933369380581036062>")
                        em.description=f"\n\n**Message Content** = ```{message.content}```"
                        em.color = embed_colour
                        em.add_field(name="Suspect",value=f"{message.author.mention}")
                        em.add_field(name="Caught In Channel",value=f"{message.channel.mention}")
                        em.add_field(name="Kicked?",value="`Nope this situation it will be staff decision `")
                        em.add_field(name="User Blacklisted?",value="<a:6456down:938005779255009321>")
                        em.set_author(name=f"{message.guild.name}",url="https://discord.gg/QuGjQTHa5y",icon_url=f"{message.guild.icon}")
                        em.timestamp= datetime.now()
                        await logs.send(embed=em) 
                    if already_t is None:
                        dictlol = {'_id': message.author.id}
                        blacklisted_user.insert(dictlol)
                        logs = self.bot.get_channel(chan_info)
                        em = nextcord.Embed(title = f"<a:robber:933369380581036062> User Caught <a:robber:933369380581036062>")
                        em.description=f"\n\n**Message Content** = ```{message.content}```"
                        em.color = embed_colour
                        em.add_field(name="Suspect",value=f"{message.author.mention}")
                        em.add_field(name="Caught In Channel",value=f"{message.channel.mention}")
                        em.add_field(name="Kicked?",value="`Nope this situation it will be staff decision `")
                        em.add_field(name="User Blacklisted?",value="<a:6456down:938005779255009321>")
                        em.set_author(name=f"{message.guild.name}",url="https://discord.gg/QuGjQTHa5y",icon_url=f"{message.guild.icon}")
                        em.timestamp= datetime.now()
                        await logs.send(embed=em) 



def setup(bot):
    bot.add_cog(optfeature(bot))
    print('@everyone Mention Protection 😎 - ✔')
